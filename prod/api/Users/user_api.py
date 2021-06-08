from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/"

user_api = Blueprint("user_api", __name__)
api = Api(user_api)

class UserResource(Resource):
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id)
        return response.json()


api.add_resource(UserResource, "/users/<user_id>")