from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users"

ns = Namespace(
    name='users',
    description='All users related operations'
)


@ns.route('')
class UsersListResource(Resource):
    REGISTER_FIELDS = ("name", "lastName", "email", "password")
    MISSING_VALUES_ERROR = 'Missing values'
    REPEATED_USER_ERROR = 'User already registered'

    body_swg = ns.model('UserInput', {
        "name": fields.String(required=True, description="The user name"),
        "lastName": fields.String(
            required=True, description="The user last name"),
        "email": fields.String(required=True, description="The user email"),
        "active": fields.Boolean(required=True, description="The user status")
    })

    code_20x_swg = ns.model('UserOutput20x', {
        "id": fields.Integer(description='The user id'),
        "name": fields.String(description="The user name"),
        "lastName": fields.String(description="The user last name"),
        "email": fields.String(description="The user email"),
        "active": fields.Boolean(description="The user status")
    })

    code_400_swg = ns.model('AllUserOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })

    code_401_swg = ns.model('AllUserOutput401', {
        'status': fields.String(example=REPEATED_USER_ERROR)
    })

    @ns.marshal_with(code_20x_swg, as_list=True, code=200)
    def get(self):
        response = requests.get(URL_USERS)
        return response.json()

    @ns.expect(body_swg)
    @ns.marshal_with(code_20x_swg, code=201)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(401, REPEATED_USER_ERROR, code_401_swg)
    def post(self):
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()
