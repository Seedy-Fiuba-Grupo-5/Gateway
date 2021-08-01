from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/admins/"

ns = Namespace(
    'admins/<int:admin_id>',
    description='One user related operations'
)


@ns.route('')
@ns.param('admin_id', 'The user identifier')
class AdminResource(Resource):
    ADMIN_NOT_FOUND_ERROR = 'admin_not_found'
    REPEATED_EMAIL_ERROR = 'repeated_email'
    REQUIRED_VALUES = ['name', 'lastName', 'email', 'password', 'token']
    MISSING_VALUES_ERROR = 'missing_args'

    body_swg = ns.model('NotRequiredUserInput', {
        "name": fields.String(description="The user new name"),
        "lastName": fields.String(description="The user new last name"),
        "email": fields.String(description="The user new email"),
        "password": fields.String(description="The user new password")
    })
    code_200_swg = ns.model('UserOutput200', {
        "id": fields.Integer(description='The admin id'),
        "name": fields.String(description="The admin name"),
        "lastName": fields.String(description="The admin last name"),
        "email": fields.String(description="The admin email"),
        "active": fields.Boolean(description="The admin status")
    })
    code_404_swg = ns.model('AdminOutput404', {
        'status': fields.String(example=ADMIN_NOT_FOUND_ERROR)
    })
    code_409_swg = ns.model('AdminOutput409', {
        'status': fields.String(example=REPEATED_EMAIL_ERROR)
    })

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, ADMIN_NOT_FOUND_ERROR, code_404_swg)
    def get(self, admin_id):
        """Get admin data"""
        response = requests.get(URL_USERS+str(admin_id))
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, ADMIN_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(409, REPEATED_EMAIL_ERROR, code_409_swg)
    def patch(self, admin_id):
        """Update admin data"""
        response = requests.patch(URL_USERS+str(admin_id), json=request.get_json())
        return api_error_handler(response)
