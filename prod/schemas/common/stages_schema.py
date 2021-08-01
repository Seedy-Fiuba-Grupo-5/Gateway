from flask_restx import Model, fields

body_swg = Model('Project_stages_payload', {
    'reviewerPublicId': fields.Integer(
        description='The reviewer id who wants to set a stage completed'),
    'stageNumber': fields.String(
        description='The number of the stage to set completed (starting from number 1)')
})
