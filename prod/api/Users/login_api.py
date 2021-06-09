from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/login"

ns = Namespace(
    'users/login',
    description='Users login operations'
)


@ns.route('')
class LoginResource(Resource):
    MISSING_ARGS_ERROR = 'Missing arguments'
    WRONG_DATA_ERROR = 'Email or password incorrect'

    body_swg = ns.model('LoginInput', {
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(
            required=True, description='The user password')
    })

    code_200_swg = ns.model('LoginOutput200', {
        'email': fields.String(description='The user email'),
        'id': fields.Integer(description='The user id')
    })

    code_400_swg = ns.model('LoginOutput400', {
        'status': fields.String(example=MISSING_ARGS_ERROR)
    })

    code_401_swg = ns.model('LoginOutput401', {
        'status': fields.String(example=WRONG_DATA_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(400, MISSING_ARGS_ERROR, code_400_swg)
    @ns.response(401, WRONG_DATA_ERROR, code_401_swg)
    def post(self):
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()
