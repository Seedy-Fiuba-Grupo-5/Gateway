import os
from flask import Flask

def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    from flask_cors import CORS
    CORS(app)

    # Configuracion
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    import_blueprints(app)

    return app


def import_blueprints(app):
    from prod.api.Web.projects_list_api import projects_list_api
    app.register_blueprint(projects_list_api)
    from prod.api.project_api import project_api
    app.register_blueprint(project_api)
