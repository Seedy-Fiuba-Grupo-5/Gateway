from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
import os
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"

projects_list_api = Blueprint("projects_list_api", __name__)
api = Api(projects_list_api)

class ProjectsListResource(Resource):
    def get(self):
        response = requests.get(URL_PROJECTS)
        return response.json()

    def post(self):
        response = requests.post(URL_PROJECTS, json=request.get_json())
        return response.json()


api.add_resource(ProjectsListResource, "/projects")
