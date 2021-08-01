from flask_restx import Model, fields

code_20x_swg = Model('CommentsOutput', {
    'id': fields.Integer(required=True, description=''),
    'id_project': fields.Integer(
        required=True, description='The project id'),
    'token': fields.String(
        required=True, description='')
})

body_swg = Model('CommentProjectInput', {
    'rating': fields.Integer(required=True,
                             description='The project rating')
})
