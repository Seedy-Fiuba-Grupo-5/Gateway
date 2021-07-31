from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler
from prod.schemas.project_fund_api import ns
from prod.schemas.common.found_schema import body_swg
from prod.schemas.project_fund_api import get_models

PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_USERS = os.getenv("USERS_BACKEND_URL")
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/projects/"


@ns.route('')
@ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):

    @ns.doc(params={'token': {'in': 'query', 'type': 'string'}})
    @ns.expect(body_swg)
    @ns.response(202, get_models['202'][0], get_models['202'][1])
    @ns.response(503, get_models['503'][0], get_models['503'][1])
    def post(self, project_id):
        first_data = request.get_json()
        token = request.args.get('token')
        user_id = first_data.get('userPublicId')
        amount_ethers = first_data.get('amountEthers')
        response = requests.post(URL_USERS + '/users/auth',
                                 json={"token": token, "user_id": user_id})
        response_object, status_code = api_error_handler(response)
        if status_code != 200:
            return response_object, status_code
        new_token = response_object['token']
        url = URL_PAYMENTS + project_id + '/funds'
        response = requests.post(
            url,
            headers={"Authorization": PAYMENTS_API_KEY},
            json=first_data)
        response_obj_pay, status_code_pay = api_error_handler(response)
        response_obj_pay['token'] = new_token
        return response_obj_pay, status_code_pay
