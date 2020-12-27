from app import app, api
from flask import send_from_directory
from .ping import Ping


#
# FRONTEND
#

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/assets/<path:path>')
def static_dist(path):
    return send_from_directory('../public/assets', path)


#
# API
#

api.add_resource(Ping, '/api/ping')
