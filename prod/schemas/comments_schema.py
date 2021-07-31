from flask_restx import Namespace, fields
from .common.comments_api_schema import code_20x_swg, body_swg
from .common.errors_schema import missing_values, invalid_token, user_not_found, \
    server_error
from .common.errors_schema import MISSING_VALUES, INVALID_TOKEN, USER_NOT_FOUND, \
    SERVER_ERROR

ns = Namespace(
    'commentary/<string:project_id>',
    description='Transactions list'
)

get_models = {
    "201": ['Success', fields.List(fields.Nested(ns.model(
        code_20x_swg.name, code_20x_swg)))],
    "400": [MISSING_VALUES, ns.model(missing_values.name, missing_values)],
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)]
}

expected = {
    'payload': ns.model(body_swg.name, body_swg),
}
