from flask_restx import Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
from prod.schemas.comments_schema import ns, get_models, expected

URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/commentary/"


@ns.route('')
class ProjectCommentsResource(Resource):

    @ns.expect(expected['payload'])
    @ns.response(201, get_models['201'][0], get_models['201'][1])
    @ns.response(400, get_models['400'][0], get_models['400'][1])
    def post(self, project_id):
        response = requests.post(URL_PROJECTS + project_id,
                                 json=request.get_json())
        return api_error_handler(response)

    @ns.response(201, get_models['201'][0], get_models['201'][1])
    @ns.response(400, get_models['400'][0], get_models['400'][1])
    def get(self, project_id):
        data = request.get_json()
        if not data:
            token = request.args.get('token')
            user_id = int(request.args.get('userId'))
        else:
            token = data["token"]
            user_id = int(data["userId"])
        response = requests.get(URL_PROJECTS + project_id,
                                json={"token": token, "user_id": user_id})
        return api_error_handler(response)
