from flask import Blueprint
from flask_restful import Api, Resource
import requests
import os
URL = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"

project_api = Blueprint("project_api", __name__)
api = Api(project_api)

class ProjectResource(Resource):
    def get(self, project_id):
        response = requests.get(URL+project_id)
        return response.json()


api.add_resource(ProjectResource, "/projects/<project_id>")