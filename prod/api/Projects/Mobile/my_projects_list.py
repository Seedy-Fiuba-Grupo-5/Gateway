from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
URL_PROJETCS = 'https://seedy-fiuba-backend-projects.herokuapp.com/projects/'
URL_USERS = 'https://seedy-fiuba-backend-users.herokuapp.com/users/'

my_projects_list_api = Blueprint("my_projects_list_api", __name__)
api = Api(my_projects_list_api)

class MyProjectsListResource(Resource):
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id)
        return response.json()

'''
    def post(self, user_id):
        response = requests.post(URL, json=request.get_json())
        return response.json()
'''

api.add_resource(MyProjectsListResource, "/users/<user_id>/projects")