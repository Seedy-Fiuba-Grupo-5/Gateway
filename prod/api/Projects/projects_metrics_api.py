from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
from prod.schemas.metrics_api_schema import ns, get_models

URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects/metrics"


@ns.route('')
class UsersListResource(Resource):

    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def get(self):
        """Get all users data"""
        response = requests.get(URL_PROJECTS)
        return api_error_handler(response)
