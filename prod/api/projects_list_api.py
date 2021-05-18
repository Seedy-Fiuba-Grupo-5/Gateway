from flask import Blueprint, request
from flask_restful import Api, Resource

projects_list_api = Blueprint("projects_list_api", __name__)
api = Api(projects_list_api)


class ProjectsListResource(Resource):
    def get(self):
        return "hello"


api.add_resource(ProjectsListResource, "/projects")
