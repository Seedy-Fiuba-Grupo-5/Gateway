from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
URL_PAYMENTS = os.getenv("PAYMENTS_BACKEND_URL")+'/transactions'
PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY")

ns = Namespace(
    'transactions',
    description='Transactions list'
)


@ns.route('')
class TransactionResource(Resource):
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    code_200_swg = ns.model('TransactionsOutput', {
        'amountEthers': fields.String(description='The amount of ethers'),
        'fromPublicId': fields.String(description='The public id'),
        'fromType': fields.String(description='The type'),
        'toPublicId': fields.String(description='The public id'),
        'toType': fields.String(description='The type'),
        'transactionType': fields.String(description='The transaction type'),
        'transactionState': fields.String(description='The transaction state'),
        'createdAt': fields.String(description='The date of creation'),
        'updatedAt': fields.String(description='The date of update')
    })

    @ns.response(200, 'Success', code_200_swg)
    def get(self):
        response = requests.get(URL_PAYMENTS, params=request.args, headers={"Authorization": PAYMENTS_API_KEY})
        return api_error_handler(response)
