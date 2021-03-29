"""
This file contains definitions of models which are used by the app
"""

import datetime
from . import db


class BaseModel(db.Model):
    __abstract__ = True
    __tablename__ = None

    def __repr__(self):
        """Returns string to internal representation of the model

        ;:rtype: string
        """
        primary_key_value = ''
        if hasattr(self, 'id'):
            key_value = self.id if self.id else '[NONE]'
            primary_key_value = f' #{key_value}'
        return '<{}{}>'.format(self.get_model_name(), primary_key_value)

    @classmethod
    def get_table_name(cls):
        """Returns name of the model's table

        :rtype: string
        """
        return cls.__tablename__

    @classmethod
    def get_model_name(cls):
        """Returns name of the model.

        :rtype: string
        """
        return cls.__name__


class Channel(BaseModel):
    __tablename__ = 'channel'

    # own properties
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    # relationships
    channel_streams = db.relationship(
        'ChannelStream', back_populates='channel', lazy='noload'
    )


class ChannelStream(BaseModel):
    __tablename__ = 'channel_stream'

    # own properties
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    channel_id = db.Column(db.ForeignKey(Channel.id), nullable=False)
    url = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    # relationships
    channel = db.relationship(
        Channel.get_model_name(),
        back_populates='channel_streams',
        lazy='noload'
    )


class Playlist(BaseModel):
    __tablename__ = 'playlist'

    # own properties
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(128), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    # relationships
    playlist_items = db.relationship(
        'PlaylistItem', back_populates='playlist', lazy='noload'
    )


class PlaylistItem(BaseModel):
    __tablename__ = 'playlist_item'

    # own properties
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    channel_id = db.Column(db.ForeignKey(Channel.id), nullable=False)
    playlist_id = db.Column(db.ForeignKey(Playlist.id), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.datetime.utcnow
    )

    # relationships
    channel = db.relationship(Channel.get_model_name(), lazy='noload')
    playlist = db.relationship(
        Playlist.get_model_name(),
        back_populates='playlist_items', lazy='noload'
    )
