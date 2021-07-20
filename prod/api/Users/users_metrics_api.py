from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_USERS = os.getenv("USERS_BACKEND_URL") + "/users/metrics"

ns = Namespace(
    name='users/metrics',
    description='All users related operations'
)


@ns.route('')
class UsersListResource(Resource):
    MISSING_VALUES_ERROR = 'missing_args'
    REPEATED_USER_ERROR = 'repeated_email'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"

    body_swg = ns.model('One user input', {
        "name": fields.String(required=True, description="The user name"),
        "lastName": fields.String(
            required=True, description="The user last name"),
        "email": fields.String(required=True, description="The user email"),
        "active": fields.Boolean(required=True, description="The user status")
    })
    code_20x_swg = ns.model('One user output 20x', {
        "percentage_blocked": fields.Integer(description='The percentage of users blocked'),
        "percentage_with_project": fields.Integer(description="The percentage of users with projects"),
        "percentage_seer": fields.Integer(description="The percentage of users that are seers")
    })
    code_503_swg = ns.model('UserMetricsOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', fields.List(fields.Nested(code_20x_swg)))
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self):
        """Get all users data"""
        response = requests.get(URL_USERS)
        return api_error_handler(response)
