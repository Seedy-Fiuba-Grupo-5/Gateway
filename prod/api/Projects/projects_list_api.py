from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"

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

    @ns.marshal_with(code_20x_swg, as_list=True, code=200)
    def get(self):
        response = requests.get(URL_PROJECTS)
        return response.json()

    @ns.expect(body_swg)
    @ns.marshal_with(code_20x_swg, as_list=False, code=201)
    @ns.response(400, description=MISSING_VALUES_ERROR, model=code_400_swg)
    def post(self):
        response = requests.post(URL_PROJECTS, json=request.get_json())
        return response.json()
