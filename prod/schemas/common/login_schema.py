from flask_restx import Model, fields

body_swg = Model('One user input', {
        "name": fields.String(required=True, description="The user name"),
        "lastName": fields.String(
            required=True, description="The user last name"),
        "email": fields.String(required=True, description="The user email"),
        "active": fields.Boolean(required=True, description="The user status")
    })
code_20x_swg = Model('One user output 20x', {
        "percentage_blocked": fields.Integer(description='The percentage of users blocked'),
        "percentage_with_project": fields.Integer(description="The percentage of users with projects"),
        "percentage_seer": fields.Integer(description="The percentage of users that are seers")
})
