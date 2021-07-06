from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from google.cloud import storage
from prod import api_error_handler
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"

ns = Namespace(
    'projects',
    description='All projects related operations'
)


@ns.route('')
class ProjectsListResource(Resource):
    MISSING_VALUES_ERROR = 'Missing values'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

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
    code_503_swg = ns.model('ProjectOutput5043', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(202, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self):
        response = requests.get(URL_PROJECTS, params=request.args)
        return api_error_handler(response)
