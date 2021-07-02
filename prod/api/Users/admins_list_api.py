from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/admins"

ns = Namespace(
    name='admins',
    description='All admins related operations'
)


@ns.route('')
class UsersListResource(Resource):
    REGISTER_FIELDS = ("name", "lastName", "email", "password")
    MISSING_VALUES_ERROR = 'missing_args'
    REPEATED_USER_ERROR = 'repeated_email'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('One admin input', {
        "name": fields.String(required=True, description="The user name"),
        "lastName": fields.String(
            required=True, description="The user last name"),
        "email": fields.String(required=True, description="The user email"),
        "active": fields.Boolean(required=True, description="The user status")
    })
    code_20x_swg = ns.model('One admin output 20x', {
        "id": fields.Integer(description='The user id'),
        "name": fields.String(description="The user name"),
        "lastName": fields.String(description="The user last name"),
        "email": fields.String(description="The user email"),
        "active": fields.Boolean(description="The user status")
    })
    code_400_swg = ns.model('One admin output 400', {
        'status': fields.String(example=MISSING_VALUES_ERROR),
        'missing_args': fields.List(fields.String())
    })
    code_409_swg = ns.model('AdminOutput409', {
        'status': fields.String(example=REPEATED_USER_ERROR)
    })
    code_503_swg = ns.model('AdminOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self):
        """Get all admins data"""
        response = requests.get(URL_USERS)
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(409, 'User already exists', code_409_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self):
        """Register new admin"""
        response = requests.post(URL_USERS, json=request.get_json())
        return api_error_handler(response)
