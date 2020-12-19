"""Main entry point to the application"""

from flask import Flask
from .config import Loader as ConfigLoader

app = Flask(__name__)
app.config.update(ConfigLoader().get_config())

from app import views
