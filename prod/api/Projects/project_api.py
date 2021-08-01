from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler

from prod.schemas.project_api_schema import ns, get_models, expect_model

URL = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"
PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_USERS = os.getenv("USERS_BACKEND_URL")
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/projects/"


@ns.route('')
@ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):

    @ns.doc(params={'token': {'in': 'query', 'type': 'string'}})
    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(200, get_models['404'][0], get_models['404'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def get(self, project_id):
        data = request.get_json()
        token = None
        if data is None:
            token = request.args.get('token')
        else:
            token = data.get('token')
        response = requests.get(URL + project_id)
        project_response_body, project_status_code = api_error_handler(response)
        if project_status_code != 200:
            return project_response_body, project_status_code
        user_response_body, user_status_code = self.get_project_owner(
            project_id, token)
        if user_status_code == 200:
            response = requests.get(
                URL_USERS + '/users/' + str(user_response_body['user_id']),
                json={"token": token})
            user_response_body, user_status_code = api_error_handler(response)
            if user_status_code == 200:
                project_response_body['user'] = user_response_body
        response = requests.get(URL_PAYMENTS + project_id,
                                headers={"Authorization": PAYMENTS_API_KEY})
        payments_body, payments_status = api_error_handler(response)
        if payments_status == 200:
            project_response_body["payments"] = payments_body
        return project_response_body, project_status_code

    @ns.expect(expect_model['payload'])
    @ns.response(200, get_models['200'][0], get_models['200'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def patch(self, project_id):
        data = request.get_json()
        response_body, status_code = self.get_project_owner(project_id,
                                                            data.get('token'))
        if status_code != 200:
            return response_body, status_code
        response = requests.post(URL_USERS + '/users/auth',
                                 json={"token": data.get('token'),
                                       "user_id": response_body.get('user_id')})
        response_object, status_code = api_error_handler(response)
        if status_code != 200:
            return response_object, status_code
        response = requests.patch(
            URL + project_id,
            json=request.get_json()
        )
        return api_error_handler(response)

    def get_project_owner(self, project_id, token):
        response = requests.get(URL_USERS + '/projects/' + project_id,
                                json={"token": token})
        return api_error_handler(response)
