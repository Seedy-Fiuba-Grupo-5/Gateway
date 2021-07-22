from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/messages/"

ns = Namespace(
    name='messages/<string:user_id>',
    description='All messages related operations'
)


@ns.route('')
class UsersListResource(Resource):
    MISSING_VALUES_ERROR = 'missing_args'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('One message input', {
        "id_1": fields.String(required=True, description="The user name"),
        "message": fields.String(
            required=True, description="The user last name"),
        "token": fields.String(required=True, description="The user email"),
    })
    code_20x_swg = ns.model('One message output 20x', {
        "id_1": fields.String(description='The user id'),
        "id_2": fields.String(description='The user id'),
        "text": fields.String(description='The text in the message'),
        "dat": fields.Date(description='The date of the message')
    })
    code_503_swg = ns.model('UserMessagesOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self, user_id):
        """Get all users data"""
        data = request.get_json()
        if data is None:
            token = request.args.get('token')
        else:
            token = data["token"]
        response = requests.get(URL_USERS+user_id, json={"token": token})
        return api_error_handler(response)

    @ns.expect(body_swg)
    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def post(self, user_id):
        """Get all users data"""
        response = requests.post(URL_USERS + user_id, json=request.get_json())
        return api_error_handler(response)

