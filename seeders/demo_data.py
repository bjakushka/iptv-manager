from .base import BaseSeeder, RandomDataGenerator
from app.models import Channel, ChannelStream, Playlist, PlaylistItem


class DemoDataSeeder(BaseSeeder):
    URL_BASE_FOR_STREAMS = 'https://iptv-source.example/streams/'

    def _execute(self, *args, **kwargs):
        channel_ids = self.seed_channels(150)
        playlist_ids = self.seed_playlists(3)
        self.seed_channel_streams(channel_ids)
        self.seed_playlists_items(playlist_ids, channel_ids)

    def seed_channels(self, amount):
        """Seeds database with randomly generated Channels

        Returns list of inserted ids

        :param int amount:
        :rtype: list of int
        """
        print(f'Seeding channels: {amount} models will be inserted')

        return list(filter(None, [
            getattr(self.insert_a_channel(), 'id', None)
            for __ in range(amount)
        ]))

    def insert_a_channel(self):
        """Creates one Channel with random data

        Returns inserted instance of Channel-model.

        :rtype: Channel
        """
        name = RandomDataGenerator.get_random_sentence(
            min_words=2, max_words=3
        )
        channel = Channel(name=name)
        self.db.session.add(channel)
        self.db.session.commit()
        return channel

    def seed_channel_streams(self, channel_ids):
        """Seeds database with randomly generated ChannelStreams

        Returns list of inserted ids

        :param list of int channel_ids:
        :rtype: list of int
        """
        amount_to_insert = len(channel_ids)
        print(f'Seeding channel streams: {amount_to_insert} '
              f'models will be inserted')

        return list(filter(None, [
            getattr(self.insert_a_channel_stream(channel_id), 'id', None)
            for channel_id in channel_ids
        ]))

    def insert_a_channel_stream(self, channel_id):
        """Creates one ChannelStream with random data

        Returns inserted instance of ChannelStream-model.

        :param int channel_id:
        :rtype: ChannelStream
        """
        url = RandomDataGenerator.get_random_url(
            url_base=self.URL_BASE_FOR_STREAMS
        )
        channel_stream = ChannelStream(
            url=url,
            channel_id=channel_id
        )
        self.db.session.add(channel_stream)
        self.db.session.commit()
        return channel_stream

    def seed_playlists(self, amount):
        """Seeds database with randomly generated Playlists

        Returns list of inserted ids

        :param int amount:
        :rtype: list of int
        """
        print(f'Seeding playlists: {amount} models will be inserted')

        return list(filter(None, [
            getattr(self.insert_a_playlist(), 'id', None)
            for __ in range(amount)
        ]))

    def insert_a_playlist(self):
        """Creates one Playlist with random data

        Returns inserted instance of Playlist-model.

        :rtype: Playlist
        """
        name = RandomDataGenerator.get_random_sentence(
            min_words=3, max_words=5
        )
        playlist = Playlist(name=name)
        self.db.session.add(playlist)
        self.db.session.commit()
        return playlist

    def seed_playlists_items(self, playlists_ids, channel_ids):
        """Seeds database with random combinations of playlist and channel

        :param list of int playlists_ids:
        :param list of int channel_ids:
        """
        print('Seeding playlist items...')

        counter = 0
        for channel_id in channel_ids:
            for playlist_id in playlists_ids:
                if RandomDataGenerator.get_random_bool(2):
                    playlist_item = self.bind_channel_with_playlist(
                        channel_id, playlist_id
                    )
                    counter = counter + (playlist_item is not None)
        print(f'{counter} playlists\' items have been created')

    def bind_channel_with_playlist(self, channel_id, playlist_id):
        """Creates on instance of PlaylistItem and stores it in db

        :param int channel_id:
        :param int playlist_id:
        :rtype: PlaylistItem
        """
        playlist_item = PlaylistItem(
            channel_id=channel_id,
            playlist_id=playlist_id
        )
        self.db.session.add(playlist_item)
        self.db.session.commit()
        return playlist_item
