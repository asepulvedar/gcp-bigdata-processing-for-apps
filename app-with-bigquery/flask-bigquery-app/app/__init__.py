from flask import Flask
from google.cloud import bigquery
import os
from .routes import bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)