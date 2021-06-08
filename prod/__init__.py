import os
from flask import Flask

def create_app(script_info=None):
    # App 'Factory'

    # Instanciar la aplicacion
    app = Flask(__name__)

    import_blueprints(app)

    return app


def import_blueprints(app):
    from .api import api_base_bp, api_v1_bp
    app.register_blueprint(api_base_bp)
    app.register_blueprint(api_v1_bp)
