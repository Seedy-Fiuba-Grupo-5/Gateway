from flask_restx import Namespace, Resource, fields
import requests
import os
URL = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"

ns = Namespace(
    'projects/<int:project_id>',
    description='Project related operations'
)


@ns.route('')
@ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):
    PROJECT_NOT_FOUND_ERROR = 'The project requested could not be found'

    code_200_swg = ns.model('ProjectOutput200', {
        'id': fields.Integer(description='The project identifier'),
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

    code_404_swg = ns.model('ProjectOutput404', {
        'status': fields.String(example=PROJECT_NOT_FOUND_ERROR)
    })

    @ns.marshal_with(code_200_swg, code=200)
    @ns.response(404, description=PROJECT_NOT_FOUND_ERROR, model=code_404_swg)
    def get(self, project_id):
        response = requests.get(URL+project_id)
        return response.json()
