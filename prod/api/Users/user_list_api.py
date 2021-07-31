from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
from prod.schemas.user_list_api_schema import ns, expected, get_models, \
    post_models

PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users"
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/wallets"


@ns.route('')
class UsersListResource(Resource):

    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def get(self):
        """Get all users data"""
        response = requests.get(URL_USERS)
        return api_error_handler(response)

    @ns.expect(expected['payload'])
    @ns.response(201, post_models['201'][0], post_models['201'][1])
    @ns.response(400, post_models['400'][0], post_models['400'][1])
    @ns.response(409, post_models['409'][0], post_models['409'][1])
    @ns.response(503, post_models['503'][0], post_models['503'][1])
    def post(self):
        """Register new user"""
        response = requests.post(URL_USERS, json=request.get_json())
        user_body, user_status_code = api_error_handler(response)
        if user_status_code != 201:
            return user_body, user_status_code
        response = requests.post(URL_PAYMENTS,
                                 headers={"Authorization": PAYMENTS_API_KEY},
                                 json={"publicId": user_body.get("id")})
        payments_body, payments_status_code = api_error_handler(response)
        if payments_status_code != 201:
            return payments_body, payments_status_code
        user_body["address"] = payments_body["address"]
        user_body["privateKey"] = payments_body["privateKey"]
        return user_body, user_status_code
