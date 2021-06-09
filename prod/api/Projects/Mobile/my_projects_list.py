from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

ns = Namespace(
    'users/<string:user_id>/projects',
    description='User projects related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class MyProjectsListResource(Resource):
    MISSING_VALUES_ERROR = 'Missing values'

    body_swg = ns.model('ProjectInput', {
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
            required=True, description='The project location')
    })

    code_20x_swg = ns.model('ProjectOutput200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_400_swg = ns.model('ProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })

    @ns.response(202, 'Success', fields.List(fields.Nested(code_20x_swg)))
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id+'/projects')
        projects_list = response.json()['project_id']
        return_value = []
        for project in projects_list:
            return_value.append(requests.get(URL_PROJECTS+'/'+str(project)).json())
        return return_value, 200

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def post(self, user_id):
        response = requests.post(URL_PROJECTS, json=request.get_json())
        if response.status_code == 201:
            response = requests.post(URL_USERS+user_id+'/projects', json={"user_id": user_id, "project_id": response.json()['id']})
            if response.status_code == 201:
                return response.json()
            else:
                return "An error has occurred while associating the project to the user", 404
        return "An error has occurred while creating the project", 404
