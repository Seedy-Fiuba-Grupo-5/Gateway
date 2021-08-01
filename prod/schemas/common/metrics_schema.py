from flask_restx import Model, fields

code_20x_swg = Model('Project metrics output 20x', {
        "most_popular_type": fields.Integer(description='Most popular type of project'),
        "avg_goal": fields.Integer(description="Average project goal"),
        "avg_duration": fields.Integer(description="Average project duration in months")
})
