from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
from prod.schemas.project_list_schema import ns, expected, get_models
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects"


@ns.route('')
class ProjectsListResource(Resource):

    @ns.expect(expected['payload'])
    @ns.response(202, get_models['202'][0],get_models['202'][1])
    @ns.response(400, get_models['400'][0], get_models['400'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def get(self):
        response = requests.get(URL_PROJECTS, params=request.args)
        return api_error_handler(response)
