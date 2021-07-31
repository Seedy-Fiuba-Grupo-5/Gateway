from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
from prod.schemas.invalid_token import invalid_token
from prod.schemas.constants import INVALID_TOKEN

URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

ns = Namespace(
    'users/<string:user_id>/favorites',
    description='User favorite projects related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class MyProjectsListResource(Resource):
    MISSING_VALUES_ERROR = 'Missing values'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('FavouriteInput', {
        'project_id': fields.String(required=True, description='The project id'),
        'token': fields.String(
            required=True, description='The users token')
    })
    code_20x_swg = ns.model('FavoriteProjectOutput200', {
        'user_id': fields.Integer(description='The user identifier'),
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })
    code_400_swg = ns.model('FavoriteProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })
    code_503_swg = ns.model('FavoriteProjectOutput5043', {
        'status': fields.String(example=SERVER_ERROR)
    })
    code_401_swg = ns.model(invalid_token.name, invalid_token)

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id+'/favorites')
        aux, status_code = api_error_handler(response)
        if status_code != 200:
            return aux, status_code
        projects_list = response.json()['projects_id']
        return_value = []
        for project in projects_list:
            response = requests.get(URL_PROJECTS+str(project))
            aux, status_code = api_error_handler(response)
            if status_code != 200:
                return aux, status_code
            return_value.append(response.json())
        return return_value, 200

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(401, INVALID_TOKEN, code_401_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self, user_id):
        data = request.get_json()
        response = requests.post(URL_USERS+user_id+'/favorites', json=data)
        users_body, users_status_code = api_error_handler(response)
        if users_status_code != 201:
            return users_body, users_status_code
        response = requests.post(URL_PROJECTS+str(data["project_id"])+'/favorites', json={"user_id": user_id})
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(401, INVALID_TOKEN, code_401_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def delete(self, user_id):
        data = request.get_json()
        response = requests.delete(URL_USERS+user_id+'/favorites', json=data)
        users_body, users_status_code = api_error_handler(response)
        if users_status_code != 200:
            return users_body, users_status_code
        response = requests.delete(URL_PROJECTS + str(data["project_id"]) + '/favorites', json={"user_id": user_id})
        return api_error_handler(response)
