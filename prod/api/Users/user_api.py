from flask import Blueprint, request
from flask_restful import Api, Resource
import requests
URL_USERS = 'https://seedy-fiuba-backend-users.herokuapp.com/users/'

user_api = Blueprint("user_api", __name__)
api = Api(user_api)

class UserResource(Resource):
    def get(self, user_id):
        response = requests.get(URL_USERS+user_id)
        return response.json()


api.add_resource(UserResource, "/users/<user_id>")