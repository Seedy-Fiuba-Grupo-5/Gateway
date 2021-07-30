from flask_restx import Namespace, fields

MISSING_VALUES_ERROR = 'Missing values'
SERVER_ERROR = "503 Server Error: Service unavailable for url"
INVALID_TOKEN = 'Invalid token; Please log in again.'
USER_NOT_FOUND = 'User not found'

ns = Namespace(
    'users/<string:user_id>/projects',
    description='User projects related operations'
)

input_swg = ns.model('MyProjectsListInput', {
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(
        required=True, description='The project description'),
    'hashtags': fields.String(
        required=True, description='The project hashtags'),
    'type': fields.String(required=True, description='The project types'),
    'goal': fields.Integer(
        required=True, description='The project goal'),
    'endDate': fields.String(
        required=True, description='The project end date'),
    'location': fields.String(
        required=True, description='The project location'),
    'lat': fields.Float(
        required=True, description='The location latitude'),
    'lon': fields.Float(
        required=True, description='The location longitude')
})

code_20x_swg = ns.model('MyProjectOutput200', {
    'id': fields.Integer(description='The project identifier'),
    'name': fields.String(required=True, description='The project name'),
    'description': fields.String(
        required=True, description='The project description'),
    'hashtags': fields.String(
        required=True, description='The project hashtags'),
    'type': fields.String(required=True, description='The project types'),
    'goal': fields.Integer(
        required=True, description='The project goal'),
    'endDate': fields.String(
        required=True, description='The project end date'),
    'location': fields.String(
        required=True, description='The project location'),
    'lat': fields.Float(
        required=True, description='The location latitude'),
    'lon': fields.Float(
        required=True, description='The location longitude')
})
code_400_swg = ns.model('ProjectOutput400', {
    'status': fields.String(example=MISSING_VALUES_ERROR)
})
code_503_swg = ns.model('ProjectOutput5043', {
    'status': fields.String(example=SERVER_ERROR)
})
code_401_swg = ns.model('InvalidToken', {
    'status': fields.Integer(example=INVALID_TOKEN)
})

code_404_swg = ns.model('UserNotFound',{
    'status': fields.String()
})
