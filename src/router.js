import Vue from 'vue';
import Router from 'vue-router';

// noinspection JSUnresolvedFunction
Vue.use(Router);

const router = new Router({
    //
    // ROUTES
    //

    routes: [
        // auxiliary pages
        {
            path: '*',
            name: 'not-found',
            component: () => import('./pages/auxiliary/NotFound.vue'),
            meta: {
                redirect: '/not-found',
            },
        },
        // regular pages
        {
            path: '/',
            name: 'dashboard',
            component: () => import('./pages/Dashboard.vue')
        },
        {
            path: '/playlist/:id',
            name: 'playlist-view',
            component: () => import('./pages/PlaylistView.vue')
        },
    ],


    //
    // CONFIGURATION
    //

    mode: 'history',
});

export default router;
