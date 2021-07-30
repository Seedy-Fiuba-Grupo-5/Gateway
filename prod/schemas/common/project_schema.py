from flask_restx import Model, fields
from .constants import PROJECT_DESCRIPTIONS

project_in = Model('ProjectInput', {
    'id': fields.Integer(description=PROJECT_DESCRIPTIONS['id']),
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name']),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description']),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags']),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type']),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal']),
    'stagesCost': fields.Integer(description=PROJECT_DESCRIPTIONS['stagesCost']),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate']),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location']),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image']),
    'video': fields.String(description=PROJECT_DESCRIPTIONS['video']),
    'path': fields.String(description=PROJECT_DESCRIPTIONS['path']),
    'lat': fields.Float(description=PROJECT_DESCRIPTIONS['lat']),
    'lon': fields.Float(description=PROJECT_DESCRIPTIONS['lon']),
})

project_min_out = Model('ProjectMinOutput', {
    'id': fields.Integer(description=PROJECT_DESCRIPTIONS['id']),
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name']),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description']),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags']),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type']),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal']),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate']),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location']),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image'])
})

project_full_out = Model('ProjectFullOutput', {
    'id': fields.Integer(description=PROJECT_DESCRIPTIONS['id']),
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name']),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description']),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags']),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type']),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal']),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate']),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location']),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image'])
})
