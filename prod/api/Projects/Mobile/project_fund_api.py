from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
from prod import api_error_handler

PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")
URL_USERS = os.getenv("USERS_BACKEND_URL")
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL") + "/projects/"

ns = Namespace(
    'projects/<string:project_id>/funds',
    description='Project funds related operations'
)

@ns.route('')
@ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):
    SUCCESS = 'Transaction being mined'
    PROJECT_NOT_FOUND_ERROR = 'The project requested could not be found'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    body_swg = ns.model('Project_Fund_Payload', {
        'userPublicId': fields.Integer(description='The user id who wants to fund'),
        'amountEthers': fields.String(description='The amount of ethers to fund')
    })
    code_202_swg = ns.model('Project_Funded_Success', {
        'id': fields.Integer(description='The transaction Id'),
        'amountEthers': fields.String(description='The amount of ethers fund'),
        'fromPublicId': fields.String(description='The id of the user funder'),
        'fromType': fields.String(example='user'),
        'toPublicId': fields.String(description='The id of the project being fund'),
        'toType': fields.String(example='project'),
        'transactionType': fields.String(example='fund'),
        'transationState': fields.String(example='mining / done'),
        'token': fields.String(description='Updated token')
    })
    code_503_swg = ns.model('ProjectOutput503', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.doc(params={'token': {'in': 'query', 'type': 'string'}})
    @ns.expect(body_swg)
    @ns.response(202, SUCCESS, code_202_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
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
        url = URL_PAYMENTS+project_id+'/funds'
        response = requests.post(
            url,
            headers={"Authorization": PAYMENTS_API_KEY},
            json=first_data)
        response_obj_pay, status_code_pay = api_error_handler(response)
        response_obj_pay['token'] = new_token
        return response_obj_pay, status_code_pay
