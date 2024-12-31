import requests
import json
from flask import Blueprint, render_template, request, redirect, url_for
from google.oauth2 import service_account

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/submit', methods=['POST'])
def submit():
    sku = request.form['sku']
    name = request.form['name']
    price = request.form['price']
    
    credentials = service_account.Credentials.from_service_account_file('/Users/asepulvedarcoppel.com/.config/gcloud/application_default_credentials.json')
    access_token = credentials.token

    url = f'https://bigquery.googleapis.com/bigquery/v2/projects/cpl-cs-lakeh-dev-01082024/datasets/ml_demos/tables/products/insertAll'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'rows': [
            {
                'json': {
                    'sku': sku,
                    'name': name,
                    'price': price
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return redirect(url_for('main.index'))
    else:
        return f'Error inserting rows: {response.text}', 500