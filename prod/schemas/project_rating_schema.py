from flask_restx import Namespace, fields
from .common.rating_schema import body_swg
from .common.errors_schema import server_error, missing_values, invalid_token
from .common.errors_schema import SERVER_ERROR, MISSING_VALUES, SUCCESS

ns = Namespace(
    'projects/<string:project_id>/rate',
    description='Transactions list'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "201": [SUCCESS, fields.List(fields.Nested(ns.model(body_swg.name,
                                                        body_swg)))],
    "400": [MISSING_VALUES, ns.model(missing_values.name, missing_values)],
}


