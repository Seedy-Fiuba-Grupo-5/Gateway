from flask_restx import Namespace, fields
from .common.stages_schema import body_swg
from .common.errors_schema import server_error
from .common.errors_schema import SERVER_ERROR, SUCCESS

ns = Namespace(
    'projects/<string:project_id>/stages',
    description='Project stages related operations'
)

post_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "202": [SUCCESS, fields.List(fields.Nested(ns.model(body_swg.name,
                                                        body_swg)))]
}
