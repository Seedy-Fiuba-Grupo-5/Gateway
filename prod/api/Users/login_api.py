from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/login"

login_api = Blueprint("login_api", __name__)
api = Api(login_api)

class LoginResource(Resource):
    def post(self):
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()


api.add_resource(LoginResource, "/users/login")