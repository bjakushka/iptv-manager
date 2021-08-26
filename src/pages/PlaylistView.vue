<template>
  <h1 v-text="playlist.name"></h1>
</template>

<script>
    import api from '../core/api.js';
    import Playlist from '../models/plyalist.js';

    // noinspection JSUnusedGlobalSymbols
    export default {
        data() {
            return {
                playlist: new Playlist({}),
            }
        },

        created() {
            let playlistId = this.$route.params.id;
            api.get(`/api/playlists/${playlistId}`).then(response => {
                this.playlist = new Playlist(response.data);
                debugger;
            });
        },

    };
</script>