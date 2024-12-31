# Flask BigQuery App

This is a demo Flask application that allows users to input SKU data through a web form and insert it into a BigQuery table using the BigQuery REST API.

## Prerequisites

- Python 3.6+
- Google Cloud Project with BigQuery API enabled
- Service account with BigQuery permissions
- Flask
- Requests library

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-bigquery-app.git
    cd flask-bigquery-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Update the `routes.py` file with your service account file path and BigQuery project details.

5. Create a `config.py` file with your configuration settings (if needed).

6. Run the Flask application:
    ```sh
    export FLASK_APP=flask-bigquery-app.app:create_app
    export FLASK_ENV=development
    flask run
    ```

7. Open your browser and navigate to `http://127.0.0.1:5000/`.

## BigQuery Table DDL

Create the BigQuery table using the following DDL:

```sql
CREATE TABLE `your_project_id.your_dataset.products` (
    sku STRING,
    name STRING,
    description STRING,
    price FLOAT
);