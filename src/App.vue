<template>
  <div class="min-h-screen bg-blue-100">

    <nav class="bg-gray-800">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex items-center justify-between h-16">
          <div class="flex items-center">
            <div class="md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <router-link
                    :to="{name: 'dashboard'}"
                    class="app--nav-item app--nav-item-active">Dashboard
                </router-link>
                <router-link
                    :to="{path: 'channels'}"
                    class="app--nav-item app--nav-item-default">All Channels
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <main>
      <div class="max-w-7xl mx-auto py-6">
        <!-- components matched by the route will render here -->
        <router-view/>
      </div>
    </main>
  </div>
</template>

<script>
    export default {
        name: 'app',
    };
</script>
