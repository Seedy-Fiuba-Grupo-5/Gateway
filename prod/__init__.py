import os
from flask import Flask

def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    import_blueprints(app)

    return app


def import_blueprints(app):
    # API
    from .api import api_base_bp, api_v1_bp
    app.register_blueprint(api_base_bp)
    app.register_blueprint(api_v1_bp)

    # TODO: Migrar a swagger style
    from prod.api.Users.user_list_api import users_list_api
    app.register_blueprint(users_list_api)

    from prod.api.Users.user_api import user_api
    app.register_blueprint(user_api)

    from prod.api.Users.login_api import login_api
    app.register_blueprint(login_api)
