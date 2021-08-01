from flask_restx import Namespace, fields
from .common.metrics_schema import code_20x_swg
from .common.errors_schema import server_error, user_not_found
from .common.errors_schema import SERVER_ERROR, USER_NOT_FOUND, SUCCESS


ns = Namespace(
    name='projects/metrics',
    description='All projects metrics'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "200": [SUCCESS, fields.List(fields.Nested(ns.model(code_20x_swg.name,
                                                        code_20x_swg)))]
}
