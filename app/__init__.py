"""Main entry point to the application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from .config import Loader as ConfigLoader

app = Flask(__name__, static_folder='../public')
app.config.update(ConfigLoader().get_config())
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from . import views  # noqa: E402 F401


def create_app():
    return app
