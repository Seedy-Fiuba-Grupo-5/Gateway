from flask_restx import Model, fields

body_swg = Model('RatingProjectInput', {
    'rating': fields.Integer(required=True, description='The project rating')
})
