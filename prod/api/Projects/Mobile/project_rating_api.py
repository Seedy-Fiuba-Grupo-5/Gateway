from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"

ns = Namespace(
    'projects/<string:project_id>/rate',
    description='Transactions list'
)


@ns.route('')
class ProjectRatingResource(Resource):
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    MISSING_VALUES_ERROR = 'Missing values'
    code_20x_swg = ns.model('RatingsOutput', {
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
            required=True, description='The project location'),
        'lat': fields.Float(
            required=True, description='The location latitude'),
        'lon': fields.Float(
            required=True, description='The location longitude'),
        'rating': fields.Integer(required=True, description='The project rating')
    })
    body_swg = ns.model('RatingProjectInput', {
        'rating': fields.Integer(required=True, description='The project rating')
    })
    code_400_swg = ns.model('RatingProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def post(self, project_id):
        response = requests.post(URL_PROJECTS+project_id+"/rate", json=request.get_json())
        return api_error_handler(response)
