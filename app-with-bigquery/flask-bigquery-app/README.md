# Flask BigQuery App

This project is a simple web application built using Flask that allows users to input SKU data into a Google BigQuery table. The application provides a user-friendly interface for submitting SKU information, which is then processed and stored in BigQuery.

## Project Structure

```
flask-bigquery-app
├── app
│   ├── static
│   │   └── styles.css
│   ├── templates
│   │   └── index.html
│   ├── __init__.py
│   └── routes.py
├── requirements.txt
├── config.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-bigquery-app
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure your Google Cloud credentials:**
   Ensure you have set up your Google Cloud project and have the necessary credentials to access BigQuery. Set the environment variable for your Google application credentials:
   ```
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
   ```

5. **Run the application:**
   ```
   python -m flask run
   ```

6. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage

- The main page will display a form where users can input SKU data.
- Upon submission, the data will be sent to the backend and inserted into the specified BigQuery table.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.