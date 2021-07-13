from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler

URL_USERS = os.getenv("USERS_BACKEND_URL") + "/seers/"

ns = Namespace(
    'seers/<string:user_id>',
    description='All seers related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    USER_NOT_FOUND_ERROR = 'user_not_found'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('NotRequiredUserInput', {
        "token": fields.String(description="The user token"),
        "project_id": fields.String(description="The project id")
    })
    code_200_swg = ns.model('UserOutput200', {
        "user_id": fields.Integer(description='The user id'),
        "project_id": fields.String(description="The project id"),
        "accepted": fields.Boolean(description="The seer request status"),
    })
    code_404_swg = ns.model('UserOutput404', {
        'status': fields.String(example=USER_NOT_FOUND_ERROR)
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
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def patch(self, user_id):
        """Update user data"""
        response = requests.patch(URL_USERS+user_id, json=request.get_json())
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, USER_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self, user_id):
        """Update user data"""
        response = requests.post(URL_USERS + user_id, json=request.get_json())
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, USER_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def delete(self, user_id):
        """Update user data"""
        response = requests.delete(URL_USERS + user_id, json=request.get_json())
        return api_error_handler(response)
