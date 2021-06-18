from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"
SERVER_ERROR_MESSAGE = "Internal server error, it looks like the Project API is down"

ns = Namespace(
    'projects',
    description='All projects related operations'
)


@ns.route('')
class ProjectsListResource(Resource):
    MISSING_VALUES_ERROR = 'Missing values'

    body_swg = ns.model('ProjectInput', {
        'name': fields.String(required=True, description='The project name'),
        'description': fields.String(
            required=True, description='The project description'),
        'hashtags': fields.String(
            required=True, description='The project hashtags'),
        'type': fields.String(required=True, description='The project types'),
        'goal': fields.Integer(required=True, description='The project goal'),
        'endDate': fields.String(
            required=True, description='The project end date'),
        'location': fields.String(
            required=True, description='The project location')
    })

    code_20x_swg = ns.model('ProjectOutput20x', {
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

    @ns.response(202, 'Sucess', fields.List(fields.Nested(code_20x_swg)))
    def get(self):
        response = requests.get(URL_PROJECTS)
        if response:
            return response.json(), response.status_code
        return SERVER_ERROR_MESSAGE, 500

    @ns.expect(body_swg)
    @ns.response(201, 'Sucess', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def post(self):
        response = requests.post(URL_PROJECTS, json=request.get_json())
        if response:
            return response.json(), response.status_code
        return SERVER_ERROR_MESSAGE, 500
