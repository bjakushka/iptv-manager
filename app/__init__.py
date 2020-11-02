"""Main entry point to the application"""

from flask import Flask

app = Flask(__name__)

from app import views
