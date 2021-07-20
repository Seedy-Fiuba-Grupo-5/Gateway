from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL")
URL_USERS = os.getenv("USERS_BACKEND_URL")
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL")

ns = Namespace(
    'services',
    description='Service status validation'
)


@ns.route('')
class ProjectResource(Resource):
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    code_200_swg = ns.model('ServerOutput', {
        'service': fields.String(description='The service name'),
        'url': fields.String(description='The service url'),
        'status': fields.String(description='The server status (Active/ Inactive)')
    })

    @ns.response(200, 'Success', code_200_swg)
    def get(self):
        response_body = []
        response_body.append(self.check_backend_projects())
        response_body.append(self.check_backend_users())
        response_body.append(self.check_backend_payments())
        return response_body, 200

    def check_backend_projects(self):
        response = requests.get(URL_PROJECTS+'/projects')
        response_body, response_status = api_error_handler(response)
        if response_status < 500:
            return {'service': 'Backend Projects', 'url': URL_PROJECTS, 'status': 'Active'}
        return {'service': 'Backend Projects', 'url': URL_PROJECTS, 'status': 'Inactive'}

    def check_backend_users(self):
        response = requests.get(URL_USERS+'/users')
        response_body, response_status = api_error_handler(response)
        if response_status < 500:
            return {'service': 'Backend Users', 'url': URL_USERS, 'status': 'Active'}
        return {'service': 'Backend Users', 'url': URL_USERS, 'status': 'Inactive'}

    def check_backend_payments(self):
        response = requests.get(URL_PAYMENTS + "/wallets",
                                headers={"Authorization": 'Bearer e67d2be7-91fe-47ce-8c15-5f726526ae07'})
        response_body, response_status = api_error_handler(response)
        if response_status < 500:
            return {'service': 'Backend Payments', 'url': URL_PAYMENTS, 'status': 'Active'}
        return {'service': 'Backend Payments', 'url': URL_PAYMENTS, 'status': 'Inactive'}


