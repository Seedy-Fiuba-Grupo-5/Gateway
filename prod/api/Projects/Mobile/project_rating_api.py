from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
from prod.schemas.common.project_schema import project_rating
from prod.schemas.common.rating_schema import body_swg
from prod.schemas.project_rating_schema import ns, get_models
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"


@ns.route('')
class ProjectRatingResource(Resource):
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    MISSING_VALUES_ERROR = 'Missing values'

    @ns.expect(body_swg)
    @ns.response(201, get_models['201'][0], get_models['201'][1])
    @ns.response(400, get_models['400'][0], get_models['400'][1])
    def post(self, project_id):
        response = requests.post(URL_PROJECTS+project_id+"/rate", json=request.get_json())
        return api_error_handler(response)

    @ns.response(201, get_models['201'][0], get_models['201'][1])
    @ns.response(400, get_models['400'][0], get_models['400'][1])
    def get(self, project_id):
        response = requests.get(URL_PROJECTS + project_id + "/rate", params=request.args)
        return api_error_handler(response)
