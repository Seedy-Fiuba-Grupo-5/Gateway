from flask_restx import Namespace, fields
from .common.project_schema import project_rating
from .common.errors_schema import server_error, missing_values
from .common.errors_schema import SERVER_ERROR, MISSING_VALUES, SUCCESS

ns = Namespace(
    'projects/<string:project_id>/rate',
    description='Transactions list'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "201": [SUCCESS, fields.List(fields.Nested(ns.model(project_rating.name,
                                                        project_rating)))],
    "400": [MISSING_VALUES, ns.model(missing_values.name, missing_values)],
}


