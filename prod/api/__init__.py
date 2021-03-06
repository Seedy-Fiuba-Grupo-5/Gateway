from flask import Blueprint
from flask_restx import Api

# Namespaces
from .Projects.Mobile.my_projects_list import ns as my_projects_list_ns
from .Projects.project_api import ns as project_ns
from .Projects.projects_list_api import ns as projects_list_ns
from prod.api.Admins.admins_list_api import ns as admins_list_ns
from prod.api.Admins.admins_login_api import ns as admins_login_ns
from prod.api.Admins.admin_api import ns as admin_ns
from .Users.login_api import ns as login_ns
from .Users.user_api import ns as user_ns
from .Users.user_list_api import ns as user_list_ns
from prod.api.Admins.admin_block_user_api import ns as admin_block_user_ns
from .service_api import ns as services_ns
from .Users.seers_api import ns as seers_ns
from .Users.users_metrics_api import ns as users_metrics_ns
from .Projects.projects_metrics_api import ns as projects_metrics_ns
from .Users.user_messages_api import ns as messages_ns
from .Projects.Mobile.favourite_projects_api import ns as favorites_ns
from .Projects.Mobile.project_fund_api import ns as project_fund_ns
from .Projects.Mobile.project_stages_api import ns as project_stages_ns
from .transactions_api import ns as transactions_ns
from .Projects.Mobile.project_rating_api import ns as rate_ns
from .Projects.project_comments_api import ns as comments_ns

NAMESPACES = (
    my_projects_list_ns,
    project_ns,
    projects_list_ns,
    login_ns,
    user_ns,
    user_list_ns,
    admins_list_ns,
    admins_login_ns,
    admin_ns,
    admin_block_user_ns,
    services_ns,
    seers_ns,
    users_metrics_ns,
    projects_metrics_ns,
    messages_ns,
    favorites_ns,
    project_fund_ns,
    project_stages_ns,
    transactions_ns,
    rate_ns,
    comments_ns
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
