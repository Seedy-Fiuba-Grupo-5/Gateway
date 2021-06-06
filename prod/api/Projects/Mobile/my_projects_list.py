from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
URL_PROJETCS = 'https://seedy-fiuba-backend-projects.herokuapp.com/projects'
URL_USERS = 'https://seedy-fiuba-backend-users.herokuapp.com/users/'

my_projects_list_api = Blueprint("my_projects_list_api", __name__)
api = Api(my_projects_list_api)

class MyProjectsListResource(Resource):
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id+'/projects')
        projects_list = response.json()['project_id']
        return_value = []
        for project in projects_list:
            return_value.append(requests.get(URL_PROJETCS+'/'+str(project)).json())
        return return_value

    def post(self, user_id):
        response = requests.post(URL_PROJETCS, json=request.get_json())
        if response.status_code == 201:
            requests.post(URL_USERS+user_id+'/projects', json={"project_id": response.json()['id']})
        return response.json()


api.add_resource(MyProjectsListResource, "/users/<user_id>/projects")