from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
import os
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users"

users_list_api = Blueprint("users_list_api", __name__)
api = Api(users_list_api)

class UsersListResource(Resource):
    def get(self):
        response = requests.get(URL_USERS)
        return response.json()

    def post(self):
        response = requests.post(URL_USERS, json=request.get_json())
        return response.json()


api.add_resource(UsersListResource, "/users")