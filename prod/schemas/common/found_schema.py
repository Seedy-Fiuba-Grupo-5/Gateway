from flask_restx import Model, fields

body_swg = Model('Project_Fund_Payload', {'userPublicId': fields.Integer(
        description='The user id who wants to fund'),
    'amountEthers': fields.String(description='The amount of ethers to fund')
})

code_202_swg = Model('Project_Funded_Success', {
        'id': fields.Integer(description='The transaction Id'),
        'amountEthers': fields.String(description='The amount of ethers fund'),
        'fromPublicId': fields.String(description='The id of the user funder'),
        'fromType': fields.String(example='user'),
        'toPublicId': fields.String(description='The id of the project'
                                                'being fund'),
        'toType': fields.String(example='project'),
        'transactionType': fields.String(example='fund'),
        'transactionState': fields.String(example='mining / done'),
        'token': fields.String(description='Updated token')
    })
