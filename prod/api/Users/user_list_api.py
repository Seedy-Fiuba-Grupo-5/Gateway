from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users"
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/wallets"

ns = Namespace(
    name='users',
    description='All users related operations'
)


@ns.route('')
class UsersListResource(Resource):
    MISSING_VALUES_ERROR = 'missing_args'
    REPEATED_USER_ERROR = 'repeated_email'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('One user input', {
        "name": fields.String(required=True, description="The user name"),
        "lastName": fields.String(
            required=True, description="The user last name"),
        "email": fields.String(required=True, description="The user email"),
        "active": fields.Boolean(required=True, description="The user status")
    })
    code_20x_swg = ns.model('One user output 20x', {
        "id": fields.Integer(description='The user id'),
        "name": fields.String(description="The user name"),
        "lastName": fields.String(description="The user last name"),
        "email": fields.String(description="The user email"),
        "active": fields.Boolean(description="The user status")
    })
    code_400_swg = ns.model('One user output 400', {
        'status': fields.String(example=MISSING_VALUES_ERROR),
        'missing_args': fields.List(fields.String())
    })
    code_409_swg = ns.model('UserOutput409', {
        'status': fields.String(example=REPEATED_USER_ERROR)
    })
    code_503_swg = ns.model('UserOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self):
        """Get all users data"""
        response = requests.get(URL_USERS)
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    @ns.response(409, 'User already exists', code_409_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self):
        """Register new user"""
        response = requests.post(URL_USERS, json=request.get_json())
        user_body, user_status_code = api_error_handler(response)
        if user_status_code is not 201:
            return user_body, user_status_code
        response = requests.post(URL_PAYMENTS,
                                 headers={"Authorization": 'Bearer e67d2be7-91fe-47ce-8c15-5f726526ae07'},
                                 json={"publicId": user_body.get("id")})
        payments_body, payments_status_code = api_error_handler(response)
        if payments_status_code is not 201:
            return payments_body, payments_status_code
        user_body["address"] = payments_body["address"]
        user_body["privateKey"] = payments_body["privateKey"]
        return user_body, user_status_code
