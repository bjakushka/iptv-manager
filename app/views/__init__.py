from app import app, api
from flask import send_from_directory
# resources
from .ping import Ping
from .playlist import PlaylistList, PlaylistOne

#
# API
#

api.add_resource(
    Ping,
    '/api/ping'
)
api.add_resource(
    PlaylistList,
    '/api/playlists',
    endpoint='playlist'
)
api.add_resource(
    PlaylistOne,
    '/api/playlists/<int:id>',
    endpoint='playlist-item'
)


@app.route('/api/<path:__>')
@app.route('/api/', defaults={'__': ''})
@app.route('/api', defaults={'__': ''})
def all_api(__):
    # for all not defined api-endpoints
    # return empty json-response with NOT FOUND status code
    return app.response_class(
        response='{}',
        status=404,
        mimetype='application/json'
    )


#
# FRONTEND
#

@app.route('/', methods=['GET'], defaults={'__': ''})
@app.route('/<path:__>', methods=['GET'])
def index(__):
    # return `index.html` with vue.js for everything except `/api*`
    return app.send_static_file('index.html')


@app.route('/assets/<path:path>')
def static_dist(path):
    return send_from_directory('../public/assets', path)
