from flask_restx import Namespace, fields
from .common.project_list_schema import body_swg, code_20x_swg
from .common.errors_schema import server_error, missing_values, invalid_token
from .common.errors_schema import SERVER_ERROR, MISSING_VALUES, INVALID_TOKEN, \
    SUCCESS

ns = Namespace(
    'projects',
    description='All projects related operations'
)

get_models = {
    "202": [SUCCESS, fields.List(fields.Nested(ns.model(code_20x_swg.name,
                                                        code_20x_swg)))],
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "400": [MISSING_VALUES, ns.model(missing_values.name, missing_values)],
}

expected = {
    'payload': ns.model(body_swg.name, body_swg)
}
