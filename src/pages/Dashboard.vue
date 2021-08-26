<template>
  <div class="flex flex-col sm:px-10">
    <table class="min-w-full divide-y">

      <thead class="bg-gray-100 text-xs font-medium text-gray-500 uppercase tracking-wider">
      <tr>
        <th scope="col"
            class="px-3 py-2 text-left w-2/3">
          Title
        </th>
        <th scope="col"
            class="px-3 py-2 text-right">
          Last modified
        </th>
      </tr>
      </thead>

      <tbody class="bg-white divide-y">
      <tr v-if="hasNotPlaylists">
        <td colspan=2 class="px-3 py-2 text-gray-900 text-center">
          NO DATA
        </td>
      </tr>
      <tr v-for="item in playlists" v-bind:key="item.name"
          @click="clickOnPlaylist(item)"
          class="cursor-pointer hover:bg-gray-100">
        <td class="px-3 py-2 whitespace-nowrap text-left">
          <span class="text-gray-900" v-text="item.name"></span>
        </td>
        <td class="px-3 py-2 whitespace-nowrap text-right">
          <span
              class="text-gray-500"
              v-text="item.updatedAt.toReadable()"
          ></span>
        </td>
      </tr>
      </tbody>

    </table>
  </div>
</template>

<script>
    import api from '../core/api.js';
    import Playlist from '../models/plyalist.js';

    // noinspection JSUnusedGlobalSymbols
    export default {
        data() {
            return {
                playlists: [],
            }
        },

        created() {
            api.get('/api/playlists').then(response => {
                this.playlists = Playlist.list(response.data);
            });
        },

        computed: {
            hasNotPlaylists() {
                return this.playlists && this.playlists.length === 0;
            }
        },

        methods: {
            clickOnPlaylist(playlist) {
                this.$router.push({
                    name: 'playlist-view',
                    params: {id: playlist.id},
                }).then();
            }
        },
    };
</script>
