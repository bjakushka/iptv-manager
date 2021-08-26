from flask_restful import Resource, fields, marshal
from sqlalchemy.orm import subqueryload_all

from ..models import Playlist as PlaylistModel

channel_stream_fields = {
    'id': fields.Integer,
    'channel_id': fields.Integer,
    'url': fields.String,
    'createdAt': fields.DateTime(
        attribute='created_at',
        dt_format='iso8601'
    ),
    'updatedAt': fields.DateTime(
        attribute='updated_at',
        dt_format='iso8601'
    ),
}

channel_fields = {
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
    'channel_streams': fields.Nested(channel_stream_fields)
}

playlist_item_fields = {
    'id': fields.Integer,
    'channel_id': fields.Integer,
    'playlist_id': fields.Integer,
    'createdAt': fields.DateTime(
        attribute='created_at',
        dt_format='iso8601'
    ),
    'updatedAt': fields.DateTime(
        attribute='updated_at',
        dt_format='iso8601'
    ),
    'channel': fields.Nested(channel_fields)
}

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
    'playlist_items': fields.Nested(playlist_item_fields)
}


class PlaylistList(Resource):
    def get(self):
        playlists = PlaylistModel.query.all()
        return marshal(playlists, playlist_resource_fields)


class PlaylistOne(Resource):
    def get(self, id):
        playlist = PlaylistModel.query.options(
            subqueryload_all('playlist_items.channel.channel_streams')
        ).filter_by(id=id).first()
        return marshal(playlist, playlist_resource_fields)
