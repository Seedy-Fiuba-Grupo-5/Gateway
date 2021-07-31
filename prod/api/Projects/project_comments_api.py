from flask_restx import Namespace, Resource, fields
from flask import request
import requests
import os
from prod import api_error_handler
URL_PROJECTS = os.getenv("PROJECTS_BACKEND_URL") + "/commentary/"

ns = Namespace(
    'commentary/<string:project_id>',
    description='Transactions list'
)


@ns.route('')
class ProjectCommentsResource(Resource):
    SERVER_ERROR = "503 Server Error: Service Unavailable for url"
    MISSING_VALUES_ERROR = 'Missing values'
    code_20x_swg = ns.model('CommentsOutput', {
        'id': fields.Integer(required=True, description=''),
        'id_project': fields.Integer(
            required=True, description='The project id'),
        'token': fields.String(
            required=True, description='')
    })
    body_swg = ns.model('CommentProjectInput', {
        'rating': fields.Integer(required=True, description='The project rating')
    })
    code_400_swg = ns.model('CommentProjectOutput400', {
        'status': fields.String(example=MISSING_VALUES_ERROR)
    })

    @ns.expect(body_swg)
    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def post(self, project_id):
        response = requests.post(URL_PROJECTS+project_id, json=request.get_json())
        return api_error_handler(response)

    @ns.response(201, 'Success', code_20x_swg)
    @ns.response(400, MISSING_VALUES_ERROR, code_400_swg)
    def get(self, project_id):
        data = request.get_json()
        if not data:
            token = request.args.get('token')
            user_id = int(request.args.get('userId'))
        else:
            token = data["token"]
            user_id = int(data["userId"])
        response = requests.get(URL_PROJECTS + project_id, json={"token": token, "user_id": user_id})
        return api_error_handler(response)
