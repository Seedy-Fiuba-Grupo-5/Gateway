from flask_restx import Namespace, fields
from .common.found_schema import body_swg
from .common.errors_schema import server_error, user_not_found, invalid_token
from .common.errors_schema import SERVER_ERROR, USER_NOT_FOUND, INVALID_TOKEN, \
    SUCCESS

ns = Namespace(
    'projects/<string:project_id>/funds',
    description='Project funds related operations'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "202": [SUCCESS, fields.List(fields.Nested(ns.model(body_swg.name,
                                                        body_swg)))],
    "401": [INVALID_TOKEN, ns.model(invalid_token.name, invalid_token)],
    "404": [USER_NOT_FOUND, ns.model(user_not_found.name, user_not_found)]
}


