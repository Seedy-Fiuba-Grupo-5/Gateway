
from flask import Blueprint
from flask_restx import Api
from .Projects.Mobile.my_projects_list import ns as my_projects_list_ns

# Base API

api_base_bp = Blueprint('api_base', __name__)
api_base = Api(
    api_base_bp,
    title='Gateway: API base',
    version=1.0,
    description='Gateway service operations'
)

api_base.add_namespace(my_projects_list_ns)

# API v1
V1_PREFIX = '/v1/'
api_v1_bp = Blueprint('api_v1', __name__, url_prefix=V1_PREFIX)
api_v1 = Api(
    api_v1_bp,
    title='Gateway: API v1',
    version=1.0,
    description='Gateway service operations'
)

api_v1.add_namespace(my_projects_list_ns)
