from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler

URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

ns = Namespace(
    'users/<string:user_id>',
    description='One user related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    USER_NOT_FOUND_ERROR = 'user_not_found'
    REPEATED_EMAIL_ERROR = 'repeated_email'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('NotRequiredUserInput', {
        "name": fields.String(description="The user new name"),
        "lastName": fields.String(description="The user new last name"),
        "email": fields.String(description="The user new email"),
        "password": fields.String(description="The user new password")
    })
    code_200_swg = ns.model('UserOutput200', {
        "id": fields.Integer(description='The user id'),
        "name": fields.String(description="The user name"),
        "lastName": fields.String(description="The user last name"),
        "email": fields.String(description="The user email"),
        "active": fields.Boolean(description="The user status")
    })
    code_404_swg = ns.model('UserOutput404', {
        'status': fields.String(example=USER_NOT_FOUND_ERROR)
    })
    code_409_swg = ns.model('UserOutput409', {
        'status': fields.String(example=REPEATED_EMAIL_ERROR)
    })
    code_503_swg = ns.model('UserOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, USER_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self, user_id):
        """Get user data"""
        response = requests.get(URL_USERS+user_id)
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, USER_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(409, REPEATED_EMAIL_ERROR, code_409_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def patch(self, user_id):
        """Update user data"""
        response = requests.patch(URL_USERS+user_id, json=request.get_json())
        return api_error_handler(response)
