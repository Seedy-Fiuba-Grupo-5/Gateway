from flask_restx import Namespace, fields
from .common.user_list_schema import body_swg, code_20x_swg
from .common.errors_schema import server_error, invalid_token, repeated_error
from .common.errors_schema import SERVER_ERROR, SUCCESS, INVALID_TOKEN,\
    REPEATED_USER_ERROR


ns = Namespace(
    name='users',
    description='All users related operations'
)

get_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "200": [SUCCESS, fields.List(fields.Nested(ns.model(code_20x_swg.name,
                                                        code_20x_swg)))]
}

post_models = {
    "503": [SERVER_ERROR, ns.model(server_error.name, server_error)],
    "201": [SUCCESS, fields.List(fields.Nested(ns.model(code_20x_swg.name,
                                                        code_20x_swg)))],
    "400": [INVALID_TOKEN, ns.model(invalid_token.name, invalid_token)],
    "409": [REPEATED_USER_ERROR, ns.model(repeated_error.name, repeated_error)]
}

expected = {
    'payload': ns.model(body_swg.name, body_swg)
}
