from flask_restx import Model, fields

MISSING_VALUES = 'Missing params and/or payload fields'
INVALID_TOKEN = 'Invalid token; please log in again'
USER_NOT_FOUND = 'User not found'
SERVER_ERROR = "Server Error: Service unavailable for url"
SUCCESS = 'Transaction being mined'
PROJECT_NOT_FOUND_ERROR = 'The project requested could not be found'

missing_values = Model('Missing_Values', {
    'status': fields.String(description=MISSING_VALUES)
})

invalid_token = Model('Invalid_Token', {
    'status': fields.String(description=INVALID_TOKEN)
})

user_not_found = Model('Not_Found', {
    'status': fields.String(description=USER_NOT_FOUND)
})

server_error = Model('Server_Error', {
    'status': fields.String(example=SERVER_ERROR)
})
