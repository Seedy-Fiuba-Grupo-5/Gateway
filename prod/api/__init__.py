from flask import Blueprint
from flask_restx import Api

# Namespaces
from .Projects.Mobile.my_projects_list import ns as my_projects_list_ns
from .Projects.project_api import ns as project_ns
from .Projects.projects_list_api import ns as projects_list_ns
from .Users.login_api import ns as login_ns
from .Users.user_api import ns as user_ns
from .Users.user_list_api import ns as user_list_ns

NAMESPACES = (
  my_projects_list_ns,
  project_ns,
  projects_list_ns,
  login_ns,
  user_ns,
  user_list_ns
)

# Base API

api_base_bp = Blueprint('api_base', __name__)
api_base = Api(
    api_base_bp,
    title='Gateway: API base',
    version=1.0,
    description='Gateway service operations'
)

for ns in NAMESPACES:
  api_base.add_namespace(ns)

# API v1
V1_PREFIX = '/v1/'
api_v1_bp = Blueprint('api_v1', __name__, url_prefix=V1_PREFIX)
api_v1 = Api(
    api_v1_bp,
    title='Gateway: API v1',
    version=1.0,
    description='Gateway service operations'
)

for ns in NAMESPACES:
  api_v1.add_namespace(ns)