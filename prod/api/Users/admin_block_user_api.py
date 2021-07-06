from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/admins/users/"

ns = Namespace(
    'admins/users/<int:user_id>',
    description='Admin blocking user'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class AdminResource(Resource):
    USER_NOT_FOUND_ERROR = 'user_not_found'
    REQUIRED_VALUES = ['token', "id_admin"]

    body_swg = ns.model('BlockOutput200',
                        {'id': fields.Integer(description='The admin id'),
                            'token': fields.String(description='The admin session token')})
    code_200_swg = ns.model('BlockOutput200', {
                            'id': fields.Integer(description='The user id'),
                            'token': fields.String(description='The user session token')})
    code_404_swg = ns.model('UserNotFound', {
                            'status': fields.String(example=USER_NOT_FOUND_ERROR)})

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, USER_NOT_FOUND_ERROR, code_404_swg)
    def patch(self, user_id):
        """Update admin data"""
        response = requests.patch(URL_USERS+str(user_id), json=request.get_json())
        return api_error_handler(response)