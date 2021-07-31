from flask_restx import Namespace, fields
from .common.project_schema import project_in, project_min_out
from .common.errors_schema import missing_values, invalid_token, user_not_found, server_error
from .common.errors_schema import MISSING_VALUES, INVALID_TOKEN, USER_NOT_FOUND, SERVER_ERROR

ns = Namespace(
    'users/<string:user_id>/projects',
    description='User projects related operations'
)

get_models = {
    "200": ['Success', fields.List(fields.Nested(ns.model(project_min_out.name, project_min_out)))],
    "404": [USER_NOT_FOUND, ns.model(user_not_found.name, user_not_found)],
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)]
}

post_models = {
    "payload": ns.model(project_in.name, project_in),
    "201": ['Success', ns.model(project_min_out.name, project_min_out)],
    "400": [MISSING_VALUES, ns.model(missing_values.name, missing_values)],
    "401": [INVALID_TOKEN, ns.model(invalid_token.name, invalid_token)],
    "404": [USER_NOT_FOUND, ns.model(user_not_found.name, user_not_found)],
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)]
}
