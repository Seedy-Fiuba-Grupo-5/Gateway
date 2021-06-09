from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

ns = Namespace(
    'users/<string:user_id>',
    description='One user related operations'
)


@ns.route('')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    USER_NOT_EXIST_ERROR = 'This user does not exists'

    code_200_swg = ns.model('UserOutput200', {
        "id": fields.Integer(description='The user id'),
        "name": fields.String(description="The user name"),
        "lastName": fields.String(description="The user last name"),
        "email": fields.String(description="The user email"),
        "active": fields.Boolean(description="The user status")
    })

    code_404_swg = ns.model('UserOutput404', {
        'status': fields.String(example=USER_NOT_EXIST_ERROR)
    })

    @ns.marshal_with(code_200_swg, code=200)
    @ns.response(404, USER_NOT_EXIST_ERROR, code_404_swg)
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id)
        return response.json()
