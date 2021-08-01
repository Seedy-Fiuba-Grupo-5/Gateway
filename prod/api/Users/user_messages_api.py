from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
from prod.schemas.message_schema import ns, get_models, expected
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/messages/"


@ns.route('')
class UsersListResource(Resource):
    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def get(self, user_id):
        """Get all users data"""
        data = request.get_json()
        if data is None:
            token = request.args.get('token')
        else:
            token = data["token"]
        response = requests.get(URL_USERS+user_id, json={"token": token})
        return api_error_handler(response)

    @ns.expect(expected['payload'])
    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def post(self, user_id):
        """Get all users data"""
        response = requests.post(URL_USERS + user_id, json=request.get_json())
        return api_error_handler(response)

