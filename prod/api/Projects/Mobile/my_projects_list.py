from flask_restx import Resource, fields
from flask import request
import requests
from google.cloud import storage
from prod import api_error_handler
from prod.schemas.my_projects_list_schema import ns, get_models, post_models
import logging
import os

PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/projects"


@ns.route('')
@ns.param('user_id', 'The user identifier')
class MyProjectsListResource(Resource):
    @ns.response(200, get_models["200"][0], get_models["200"][1])
    @ns.response(404, get_models["404"][0], get_models["404"][1])
    @ns.response(503, get_models["503"][0], get_models["503"][1])
    def get(self, user_id):
        response = requests.get(URL_USERS + user_id + '/projects')
        aux, status_code = api_error_handler(response)
        if status_code != 200:
            return aux, status_code
        projects_list = response.json()['project_id']
        return_value = []
        for project in projects_list:
            response = requests.get(URL_PROJECTS + '/' + str(project))
            aux, status_code = api_error_handler(response)
            if status_code != 200:
                return aux, status_code
            return_value.append(response.json())
        return return_value, 200

    @ns.expect(post_models["payload"])
    @ns.response(201, post_models["201"][0], post_models["201"][1])
    @ns.response(400, post_models["400"][0], post_models["400"][1])
    @ns.response(401, post_models["401"][0], post_models["401"][1])
    @ns.response(404, post_models["404"][0], post_models["404"][1])
    @ns.response(503, post_models["503"][0], post_models["503"][1])
    def post(self, user_id):
        data = request.get_json()
        stages_cost = data.get('stagesCost')
        token_json, token_status_code = self.validate_token(user_id)
        if token_status_code != 200:
            return token_json, token_status_code
        project_json, project_status_code = self.create_project()
        if project_status_code != 201:
            return project_json, project_status_code
        user_json, user_status_code = self.add_project_to_user(user_id,
                                                               project_json[
                                                                   'id'])
        if user_status_code != 201:
            requests.delete(URL_PROJECTS + '/' + project_json['id'])
            return user_json, user_status_code
        self.create_project_wallet(user_id, project_json.get('id'), stages_cost)
        return self.create_firebase_directory(project_json['id'])

    def create_project_wallet(self, user_id, project_id, stages_cost):
        response = requests.post(URL_PAYMENTS,
                                 headers={"Authorization": PAYMENTS_API_KEY},
                                 json={"publicId": project_id,
                                       "ownerPublicId": user_id,
                                       "reviewerPublicId": -1,
                                       "stagesCost": stages_cost})
        return api_error_handler(response)

    def validate_token(self, user_id):
        data = request.get_json()
        response = requests.post(URL_USERS + 'auth',
                                 json={"token": data.get('token'),
                                       "user_id": int(user_id)})
        return api_error_handler(response)

    def create_project(self):
        data = request.get_json()
        response = requests.post(URL_PROJECTS, json=data)
        return api_error_handler(response)

    def add_project_to_user(self, user_id, project_id):
        response = requests.post(URL_USERS + user_id + '/projects',
                                 json={"user_id": user_id,
                                       "project_id": project_id})
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
        response = requests.patch(URL_PROJECTS + '/' + str(project_id),
                                  json=patch)
        return api_error_handler(response)
