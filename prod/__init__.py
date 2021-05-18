import os
from flask import Flask

def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    # Configuracion
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    import_blueprints(app)

    return app


def import_blueprints(app):
    from .api.projects_list_api import projects_list_api
    app.register_blueprint(projects_list_api)
