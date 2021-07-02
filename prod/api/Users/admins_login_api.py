from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/admins/login"

ns = Namespace(
    'admins/login',
    description='Admins login operations'
)


@ns.route('')
class LoginResource(Resource):
    MISSING_ARGS_ERROR = 'missing_args'
    USER_NOT_FOUND_ERROR = 'user_not_found'
    WRONG_PASS_ERROR = 'wrong_password'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('AdminLoginInput', {
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(
            required=True, description='The user password')
    })
    code_200_swg = ns.model('AdminsLoginOutput200', {
        'email': fields.String(description='The user email'),
        'id': fields.Integer(description='The user id')
    })
    code_400_swg = ns.model('AdminsLoginOutput400', {
        'status': fields.String(example=MISSING_ARGS_ERROR),
        'missing_args': fields.List(fields.String())
    })
    code_401_swg = ns.model('AdminsLoginOutput401', {
        'status': fields.String(example=WRONG_PASS_ERROR)
    })
    code_404_swg = ns.model('AdminsLoginOutput404', {
        'status': fields.String(example=USER_NOT_FOUND_ERROR)
    })
    code_503_swg = ns.model('AdminsLoginOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(400, 'Missing arguments', code_400_swg)
    @ns.response(401, 'Wrong password', code_401_swg)
    @ns.response(404, 'User not found', code_404_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self):
        """Login"""
        response = requests.post(URL_USERS, json=request.get_json())
        return api_error_handler(response)
