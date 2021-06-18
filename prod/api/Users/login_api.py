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
    MISSING_ARGS_ERROR = 'missing_args'
    USER_NOT_FOUND_ERROR = 'user_not_found'
    WRONG_PASS_ERROR = 'wrong_password'

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
        'status': fields.String(example=MISSING_ARGS_ERROR),
        'missing_args': fields.List(fields.String())
    })

    code_401_swg = ns.model('LoginOutput401', {
        'status': fields.String(example=WRONG_PASS_ERROR)
    })

    code_404_swg = ns.model('LoginOutput404', {
        'status': fields.String(example=USER_NOT_FOUND_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(400, 'Missing arguments', code_400_swg)
    @ns.response(401, 'Wrong password', code_401_swg)
    @ns.response(404, 'User not found', code_404_swg)
    def post(self):
        """Login"""
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()
