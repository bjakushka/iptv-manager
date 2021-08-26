import Vue from 'vue';
import App from './App.vue';
import router from './router.js';
import './assets/styles.css';

export default new Vue({
    el: '#app',
    render: h => h(App),
    router,
});


//
// OTHER
//

/**
 * Returns string with readable representation of date.
 *
 * @returns {string}
 */
Date.prototype.toReadable = function () {
    let options = {
        weekday: 'short',
        year: "numeric",
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "numeric"
    };
    let locale = 'en-GB';

    return this.toLocaleDateString(locale, options)
};
