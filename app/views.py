from . import app
from flask import send_from_directory, jsonify


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/assets/<path:path>')
def static_dist(path):
    return send_from_directory('../public/assets', path)


@app.route('/api/ping')
def api_ping():
    return jsonify({
        'data': {
            'answer': 'pong',
        },
    })
