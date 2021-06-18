from flask import request
from flask_restx import Namespace, Resource, fields
import requests
import os
URL = os.getenv("PROJECTS_BACKEND_URL") + "/projects/"
ns = Namespace(
    'projects/<string:project_id>',
    description='Project related operations'
)


@ns.route('')
@ns.param('project_id', 'The project identifier')
class ProjectResource(Resource):
    PROJECT_NOT_FOUND_ERROR = 'The project requested could not be found'
    SERVER_ERROR = "503 Server Error: Service Unavailable for url: https://seedy-fiuba-backend-projects.herokuapp.com/projects/<project_id>"

    body_swg = ns.model('NotRequiredProjectInput', {
        'name': fields.String(description='The project name'),
        'description': fields.String(description='The project description'),
        'hashtags': fields.String(description='The project hashtags'),
        'type': fields.String(description='The project types'),
        'goal': fields.Integer(description='The project goal'),
        'endDate': fields.String(description='The project end date'),
        'location': fields.String(description='The project location')
    })

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

    code_503_swg = ns.model('ProjectOutput404', {
        'status': fields.String(example=SERVER_ERROR)
    })

    @ns.response(200, 'Success', code_200_swg)
    @ns.response(404, PROJECT_NOT_FOUND_ERROR, code_404_swg)
    @ns.response(503, SERVER_ERROR, code_503_swg)
    def get(self, project_id):
        response = requests.get(URL+project_id)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code < 500:
                return e.response.json(), e.response.status_code
            response_body = {"status": str(e)}
            return response_body, e.response.status_code
        return response.json(), response.status_code


    @ns.expect(body_swg)
    @ns.response(200, 'Success', code_200_swg)
    def patch(self, project_id):
        try:
            response = requests.patch(
                URL+project_id,
                json=request.get_json()
            )
        except requests.exceptions.RequestException as e:
            ns.abort(e)
        return response.json(), response.status_code