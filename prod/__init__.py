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
    from prod.api.Projects.projects_list_api import projects_list_api
    app.register_blueprint(projects_list_api)

    from prod.api.Projects.project_api import project_api
    app.register_blueprint(project_api)

    from prod.api.Projects.Mobile.my_projects_list import my_projects_list_api
    app.register_blueprint(my_projects_list_api)

    from prod.api.Users.user_list_api import users_list_api
    app.register_blueprint(users_list_api)

    from prod.api.Users.user_api import user_api
    app.register_blueprint(user_api)

    from prod.api.Users.login_api import login_api
    app.register_blueprint(login_api)
