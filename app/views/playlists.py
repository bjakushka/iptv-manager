from flask_restful import Resource, fields, marshal
from ..models import Playlist

playlist_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'createdAt': fields.DateTime(
        attribute='created_at',
        dt_format='iso8601'
    ),
    'updatedAt': fields.DateTime(
        attribute='updated_at',
        dt_format='iso8601'
    ),
}


class Playlists(Resource):
    def get(self):
        playlists = Playlist.query.all()
        return marshal(playlists, playlist_resource_fields)
