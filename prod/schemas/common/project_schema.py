from flask_restx import Model, fields

PROJECT_DESCRIPTIONS = {
    'id': 'The project id',
    'name': 'The project name',
    'description': 'The project description',
    'hashtags': 'The project hashtags',
    'type': 'The project type',
    'goal': 'The project goal',
    'stagesCost': 'The project stages costs',
    'endDate': 'The project end date',
    'location': 'The project location',
    'image': 'The project image url',
    'video': 'The project video url',
    'path': 'The firebase path to videos files',
    'lat': 'The location latitude',
    'lon': 'The location longitude'
}

project_in = Model('Project_Input', {
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name'], required=True),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description'], required=True),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags'], required=True),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type'], required=True),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal'], required=True),
    'stagesCost': fields.Integer(description=PROJECT_DESCRIPTIONS['stagesCost'], required=True),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate'], required=True),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location'], required=True),
    'lat': fields.Float(description=PROJECT_DESCRIPTIONS['lat'], required=True),
    'lon': fields.Float(description=PROJECT_DESCRIPTIONS['lon'], required=True),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image']),
    'video': fields.String(description=PROJECT_DESCRIPTIONS['video']),
    'path': fields.String(description=PROJECT_DESCRIPTIONS['path'])
})

project_min_out = Model('Project_Min_Output', {
    'id': fields.Integer(description=PROJECT_DESCRIPTIONS['id']),
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name']),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description']),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags']),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type']),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal']),
    'stagesCost': fields.Integer(description=PROJECT_DESCRIPTIONS['stagesCost']),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate']),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location']),
    'lat': fields.Float(description=PROJECT_DESCRIPTIONS['lat']),
    'lon': fields.Float(description=PROJECT_DESCRIPTIONS['lon']),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image']),
    'video': fields.String(description=PROJECT_DESCRIPTIONS['video']),
    'path': fields.String(description=PROJECT_DESCRIPTIONS['path'])
})

project_full_out = Model('Project_Full_Output', {
    'id': fields.Integer(description=PROJECT_DESCRIPTIONS['id']),
    'name': fields.String(description=PROJECT_DESCRIPTIONS['name']),
    'description': fields.String(description=PROJECT_DESCRIPTIONS['description']),
    'hashtags': fields.String(description=PROJECT_DESCRIPTIONS['hashtags']),
    'type': fields.String(description=PROJECT_DESCRIPTIONS['type']),
    'goal': fields.Integer(description=PROJECT_DESCRIPTIONS['goal']),
    'stagesCost': fields.Integer(description=PROJECT_DESCRIPTIONS['stagesCost']),
    'endDate': fields.String(description=PROJECT_DESCRIPTIONS['endDate']),
    'location': fields.String(description=PROJECT_DESCRIPTIONS['location']),
    'lat': fields.Float(description=PROJECT_DESCRIPTIONS['lat']),
    'lon': fields.Float(description=PROJECT_DESCRIPTIONS['lon']),
    'image': fields.String(description=PROJECT_DESCRIPTIONS['image']),
    'video': fields.String(description=PROJECT_DESCRIPTIONS['video']),
    'path': fields.String(description=PROJECT_DESCRIPTIONS['path']),
})

project_rating = Model('RatingsOutput', {
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
            required=True, description='The location longitude'),
        'rating': fields.Integer(required=True, description='The project rating')
    })
