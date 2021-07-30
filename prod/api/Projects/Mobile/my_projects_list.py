from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
from google.cloud import storage
from prod.schemas.invalid_token import invalid_token
from prod.schemas.constants import INVALID_TOKEN
import logging

PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/projects"

ns = Namespace(
    'users/<string:user_id>/projects',
    description='User projects related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class MyProjectsListResource(Resource):
    MISSING_VALUES_ERROR = 'Missing values'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('MyProjectInput', {
        'name': fields.String(required=True, description='The project name'),
        'description': fields.String(
            required=True, description='The project description'),
        'hashtags': fields.String(
            required=True, description='The project hashtags'),
        'type': fields.String(required=True, description='The project types'),
        'goal': fields.Integer(
            required=True, description='The project goal'),
        'endDate': fields.String(
            required=True, description='The project end date'),
        'location': fields.String(
            required=True, description='The project location'),
        'lat': fields.Float(
            required=True, description='The location latitude'),
        'lon': fields.Float(
            required=True, description='The location longitude')
    })

    code_20x_swg = ns.model('MyProjectOutput200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(required=True, description='The project name'),
        'description': fields.String(
            required=True, description='The project description'),
        'hashtags': fields.String(
            required=True, description='The project hashtags'),
        'type': fields.String(required=True, description='The project types'),
        'goal': fields.Integer(
            required=True, description='The project goal'),
        'endDate': fields.String(
            required=True, description='The project end date'),
        'location': fields.String(
            required=True, description='The project location'),
        'lat': fields.Float(
            required=True, description='The location latitude'),
        'lon': fields.Float(
            required=True, description='The location longitude')
    })
    code_400_swg = ns.model('ProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })
    code_503_swg = ns.model('ProjectOutput5043', {
        'status': fields.String(example=SERVER_ERROR)
    })
    code_401_swg = ns.model(invalid_token.name, invalid_token)

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id+'/projects')
        aux, status_code = api_error_handler(response)
        if status_code != 200:
            return aux, status_code
        projects_list = response.json()['project_id']
        return_value = []
        for project in projects_list:
            response = requests.get(URL_PROJECTS+'/'+str(project))
            aux, status_code = api_error_handler(response)
            if status_code != 200:
                return aux, status_code
            return_value.append(response.json())
        return return_value, 200

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(401, INVALID_TOKEN, code_401_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self, user_id):
        data = request.get_json()
        stages_cost = data.get('stagesCost')
        token_json, token_status_code = self.validate_token(user_id)
        if token_status_code != 200:
            return token_json, token_status_code
        project_json, project_status_code = self.create_project()
        if project_status_code != 201:
            return project_json, project_status_code
        user_json, user_status_code = self.add_project_to_user(user_id, project_json['id'])
        if user_status_code != 201:
            requests.delete(URL_PROJECTS + '/' + project_json['id'])
            return user_json, user_status_code
        self.create_project_wallet(user_id, project_json.get('id'), stages_cost)
        return self.create_firebase_directory(project_json['id'])

    def create_project_wallet(self, user_id, project_id, stages_cost):
        response = requests.post(URL_PAYMENTS,
                                 headers={"Authorization": PAYMENTS_API_KEY},
                                 json={"publicId": project_id, "ownerPublicId": user_id, "reviewerPublicId": -1,
                                       "stagesCost": stages_cost})
        return api_error_handler(response)

    def validate_token(self, user_id):
        data = request.get_json()
        response = requests.post(URL_USERS + 'auth', json={"token": data.get('token'), "user_id": int(user_id)})
        return api_error_handler(response)

    def create_project(self):
        data = request.get_json()
        response = requests.post(URL_PROJECTS, json=data)
        return api_error_handler(response)

    def add_project_to_user(self, user_id, project_id):
        response = requests.post(URL_USERS + user_id + '/projects',
                                 json={"user_id": user_id, "project_id": project_id})
        return api_error_handler(response)

    def create_firebase_directory(self, project_id):
        client = storage.Client()
        bucket = client.get_bucket('seedyfiuba-a983e.appspot.com')
        path = os.path.abspath(os.getcwd())
        imagePath = path + "/prod/api/Projects/default.jpg"
        storagePath = "projects/" + str(project_id) + "/images/"
        imageBlob = bucket.blob(storagePath + "default.jpg")
        imageBlob.upload_from_filename(imagePath)
        patch = {"path": storagePath}
        response = requests.patch(URL_PROJECTS + '/' + str(project_id), json=patch)
        return api_error_handler(response)
