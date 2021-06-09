from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
import os
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

my_projects_list_api = Blueprint("my_projects_list_api", __name__)
api = Api(my_projects_list_api)

class MyProjectsListResource(Resource):
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id+'/projects')
        projects_list = response.json()['project_id']
        return_value = []
        for project in projects_list:
            return_value.append(requests.get(URL_PROJECTS+'/'+str(project)).json())
        return return_value

    def post(self, user_id):
        response = requests.post(URL_PROJECTS, json=request.get_json())
        if response.status_code == 201:
            response = requests.post(URL_USERS+user_id+'/projects', json={"user_id": user_id, "project_id": response.json()['id']})
            if response.status_code == 201:
                return response.json()
            else:
                return "An error has occurred while associating the project to the user", 404
        return "An error has occurred while creating the project", 404


api.add_resource(MyProjectsListResource, "/users/<user_id>/projects")