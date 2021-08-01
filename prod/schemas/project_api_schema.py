from flask_restx import Namespace, fields
from .common.project_schema import project_api_200
from .common.errors_schema import server_error, user_not_found, invalid_token
from .common.errors_schema import SERVER_ERROR, USER_NOT_FOUND, INVALID_TOKEN, \
    SUCCESS
from prod.schemas.common.project_schema import project_model

ns = Namespace(
    'projects/<string:project_id>',
    description='Project related operations'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "200": [SUCCESS, fields.List(fields.Nested(ns.model(project_api_200.name,
                                                        project_api_200)))],
    "404": [USER_NOT_FOUND, ns.model(user_not_found.name, user_not_found)]
}

expect_model = {
    "payload": ns.model(project_model.name, project_model)
}
