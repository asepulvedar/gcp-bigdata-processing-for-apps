# %% Import Python Modules
import requests
import google.auth
from google.auth.transport.requests import Request


# %%Set variables
PROJECT_ID = "your-project-id"
REGION = "ypur-region"
BATCH_ID = "serverless-job-from-rest-api"
PYSPARK_MAIN_FILE_URI = "gs://us-central1-cpr-cs-ingdat-c-b912db76-bucket/jobs/python-scikit-learn-job-writebq-bqapi.py"
PYPSPARK_JOB_ARGS = ["1"]

CONTAINER_IMAGE = f"us-central1-docker.pkg.dev/{PROJECT_ID}/YOUR-DOCKER-REPO/YOUR-DOCKER-IMAGE"
SERVICE_ACCOUNT = "YOUR-SERVICE-ACCOUNT"
SUBNETWORK_URI = "projects/YOUR-NETWORK-PROJECT/regions/YOUR-NETWORK-REGION/subnetworks/YOUR-SUBNET-NAME"
NETWORK_TAGS = ["YOUR-NETWORK-TAG"]


# Use Application Default Credentials (ADC)
credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

# Refresh the token
credentials.refresh(Request())
access_token = credentials.token

print("Access Token:", access_token)

# %% Define the request config
DATAPROC_SUMBITBATCH_ENDPOINT = f"https://dataproc.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/batches?batchId={BATCH_ID}"

request_body = {
  "pysparkBatch": {
    "args": PYPSPARK_JOB_ARGS,
    "mainPythonFileUri": PYSPARK_MAIN_FILE_URI
  },
  "labels": {
    "goog-dataproc-batch-id": BATCH_ID,
    "goog-dataproc-location": REGION
  },
  "runtimeConfig": {
    "version": "2.2",
    "containerImage": CONTAINER_IMAGE,
    "properties": {
      "spark.driver.cores": "8",
      "spark.executor.instances": "2",
      "spark.driver.memory": "16g",
      "spark.executor.cores": "4",
      "spark.executor.memory": "9600m",
      "spark.dynamicAllocation.executorAllocationRatio": "0.3",
      "spark.app.name": f"projects/{PROJECT_ID}/locations/us-central1/batches/{BATCH_ID}",
      "spark.dataproc.scaling.version": "2"
    }
  },
  "name": f"projects/{PROJECT_ID}/locations/us-central1/batches/{BATCH_ID}",
  "environmentConfig": {
    "executionConfig": {
      "serviceAccount": SERVICE_ACCOUNT,
      "subnetworkUri": SUBNETWORK_URI,
      "networkTags": NETWORK_TAGS
    }
  }
}

# %% Send the Request to the Dataprocc REST API
response = requests.post(
    DATAPROC_SUMBITBATCH_ENDPOINT,
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    },
    json=request_body
)
# %% Response details
response_details = response.json()

print(response_details)



# %% Check the status of the batch job

# Set variables
DATAPROC_CHECK_BATCH_ENDPOINT = f"https://dataproc.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/batches/{BATCH_ID}"

# Use Application Default Credentials (ADC)
credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

# Refresh the token
credentials.refresh(Request())
access_token = credentials.token

# Send the request to the Dataproc REST API to get the batch status
response = requests.get(
    DATAPROC_CHECK_BATCH_ENDPOINT,
    headers={
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
)

# Print the response
print(response.status_code)
print(response.json())

# Batch Status 
# 1.- PENDING: The batch job has been created but has not yet started running.
# 2.- RUNNING: The batch job is currently running.
# 3.- CANCELLING: The batch job is in the process of being cancelled.
# 4.- CANCELLED: The batch job has been cancelled.
# 5.- SUCCEEDED: The batch job has completed successfully.
# 6.- FAILED: The batch job has failed.
# 7.- UNKNOWN: The status of the batch job is unknown.

