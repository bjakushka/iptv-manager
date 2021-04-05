"""Main entry point to the application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from sqlalchemy import MetaData
from .config import Loader as ConfigLoader

app = Flask(__name__, static_folder='../public')
app.config.update(ConfigLoader().get_config())

# initialize plugins and extensions
convention = {
    'ix': '%(table_name)s   _ix',
    'uq': '%(table_name)s_uq_%(column_0_name)s',
    'fk': '%(table_name)s_fk_%(referred_table_name)s',
    'pk': '%(table_name)s_pk',
}
metadata = MetaData(naming_convention=convention)
app.db = db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)
api = Api(app)

from . import views  # noqa: E402 F401
from . import models  # noqa: E402 F401


def create_app():
    return app
