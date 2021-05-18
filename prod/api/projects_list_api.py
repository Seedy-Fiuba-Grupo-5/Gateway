from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
URL = 'http://172.22.0.1:5000/projects'

projects_list_api = Blueprint("projects_list_api", __name__)
api = Api(projects_list_api)

class ProjectsListResource(Resource):
    def get(self):
        response = requests.get(URL)
        return response.json()

    def post(self):
        response = requests.post(URL, json=request.get_json())
        return response.json()


api.add_resource(ProjectsListResource, "/projects")
