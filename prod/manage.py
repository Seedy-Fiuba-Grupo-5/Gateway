from flask.cli import FlaskGroup
from prod import create_app
from flask_cors import CORS

app = create_app()
CORS(app)

cli = FlaskGroup(create_app=create_app)

if __name__ == "__main__":
    cli()
