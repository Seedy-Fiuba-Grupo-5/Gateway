from flask_restx import Model, fields

body_swg = Model('One message input', {
    "id_1": fields.String(required=True, description="The user name"),
    "message": fields.String(
        required=True, description="The user last name"),
    "token": fields.String(required=True, description="The user email"),
})
code_20x_swg = Model('One message output 20x', {
    "id_1": fields.String(description='The user id'),
    "id_2": fields.String(description='The user id'),
    "text": fields.String(description='The text in the message'),
    "dat": fields.Date(description='The date of the message')
})
