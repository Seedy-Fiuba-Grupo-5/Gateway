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

    body_swg = ns.model('Login input', {
        'email': fields.String(required=True, description='The user email'),
        'password': fields.String(
            required=True, description='The user password')
    })

    code_200_swg = ns.model('Login output 200', {
        'email': fields.String(description='The user email'),
        'id': fields.Integer(description='The user id')
    })

    code_400_swg = ns.model('Login output 400', {
        'status': fields.String(example=MISSING_ARGS_ERROR)
    })

    code_401_swg = ns.model('Login output 401', {
        'status': fields.String(example=WRONG_DATA_ERROR)
    })

    @ns.expect(body_swg)
    @ns.marshal_with(code_200_swg, code=200)
    @ns.response(code=400, description=MISSING_ARGS_ERROR, model=code_400_swg)
    @ns.response(code=401, description=WRONG_DATA_ERROR, model=code_401_swg)
    def post(self):
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()
