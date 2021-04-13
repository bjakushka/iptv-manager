import axios from 'axios';

const apiClient = axios.create({
    // wait at least N-milliseconds before failing
    timeout: 8000,
    // api base url which will be prepended to all relative urls
    baseURL: '',
});

const api = {

    /**
     * Sends `GET` request to the API.
     *
     * @param {string} relativeUrl URL of API endpoint. Relative to API base URL.
     * @returns {Promise<AxiosResponse<T>>}
     */
    get(relativeUrl) {
        return apiClient.get(relativeUrl);
    }

};

export default api;
