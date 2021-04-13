<template>
  <div class="min-h-screen bg-blue-100">

    <nav class="bg-gray-800">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <a href="#" class="app--nav-item app--nav-item-active">Dashboard</a>
                <a href="#" class="app--nav-item app--nav-item-default">All Channels</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <main>
      <div class="max-w-7xl mx-auto py-6">
        <playlists-table :playlists="playlists"/>
      </div>
    </main>
  </div>
</template>

<script>
    import api from './core/api.js';
    import PlaylistsTable from './PlaylistsTable.vue';
    import Playlist from './models/plyalist.js';

    export default {
        name: 'app',

        components: {
            PlaylistsTable
        },

        data() {
            return {
                playlists: [],
            }
        },

        created() {
            console.log('Root element of the application has been created');

            api.get('/api/playlists').then(response => {
                this.playlists = Playlist.list(response.data);
            });
        },
    };
</script>
