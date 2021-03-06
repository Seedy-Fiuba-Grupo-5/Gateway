import os
from flask import Flask
import requests
import firebase_admin
from firebase_admin import credentials

FLASK_ENV = os.getenv('FLASK_ENV')

def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    import_blueprints(app)

    if FLASK_ENV != 'development':
        create_firebase_app()

    return app

def create_firebase_app():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "prod/api/firebaseKey.json"
    cred = credentials.Certificate('prod/api/firebaseKey.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': "gs://seedyfiuba-a983e.appspot.com"
    })

def import_blueprints(app):
    from .api import api_base_bp, api_v1_bp
    app.register_blueprint(api_base_bp)
    app.register_blueprint(api_v1_bp)

def api_error_handler(response):
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code < 500:
            return e.response.json(), e.response.status_code
        response_body = {"status": str(e)}
        return response_body, e.response.status_code
    return response.json(), response.status_code
