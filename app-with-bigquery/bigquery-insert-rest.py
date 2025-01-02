# %% Import the required libraries
import requests
import json
import google.auth
from google.auth.transport.requests import Request


# Define the table and dataset
PROJECT_ID = 'your-project-id'
DATASET_ID = 'your-dataset-id'
TABLE_ID = 'your-table-id'

BIGQUERY_INSERT_ENDPOINT = f'https://www.googleapis.com/bigquery/v2/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}/insertAll'

# Use Application Default Credentials (ADC)
credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])

# Prepare the data to be inserted
rows_to_insert = [
    {"json": {"sku": "1234", "name": "pantalon", "price": 10.0}},
     {"json": {"sku": "567", "name": "camisa", "price": 7.0}},
      {"json": {"sku": "965", "name": "playera", "price": 22.0}},
]


# %% Refresh the token
credentials.refresh(Request())
access_token = credentials.token

print("Access Token:", access_token)

# %% Make the API request to insert the data
response = requests.post(
    BIGQUERY_INSERT_ENDPOINT,
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {credentials.token}'
    },
    data=json.dumps({
        "rows": rows_to_insert
    })
)

# Check the response
if response.status_code == 200:
    print('Rows successfully inserted')
else:
    print(f'Error inserting rows: {response.text}')


