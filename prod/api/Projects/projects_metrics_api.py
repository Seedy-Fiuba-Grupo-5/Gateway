from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/projects/metrics"

ns = Namespace(
    name='projects/metrics',
    description='All projects metrics'
)


@ns.route('')
class UsersListResource(Resource):
    MISSING_VALUES_ERROR = 'missing_args'
    REPEATED_USER_ERROR = 'repeated_email'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    code_20x_swg = ns.model('Project metrics output 20x', {
        "most_popular_type": fields.Integer(description='Most popular type of project'),
        "avg_goal": fields.Integer(description="Average project goal"),
        "avg_duration": fields.Integer(description="Average project duration in months")
    })
    code_503_swg = ns.model('ProjectMetricsOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self):
        """Get all users data"""
        response = requests.get(URL_PROJECTS)
        return api_error_handler(response)
