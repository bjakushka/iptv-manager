// for general purposes
const path = require('path');

//
// webpack plugins
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Webpack = require('webpack');

const PATHS = {
    sources: path.resolve(__dirname, './src'),
    dist: path.resolve(__dirname, './public'),
};

module.exports = {
    mode: 'development',

    // an application's entry point
    entry: [
        PATHS.sources + '/index.js',
    ],

    output: {
        publicPath: '/',
        path: PATHS.dist,
        filename: 'assets/app.bundle.js',
    },

    module: {
        rules: []
    },

    // used plugins
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: PATHS.sources + '/assets/index.html',
            inject: true,
            hash: true,
        }),
        // enables support for HMR (see `devServer` section)
        new Webpack.HotModuleReplacementPlugin(),
    ],

    // configuration of development server
    devServer: {
        // listen to
        host: '0.0.0.0',
        port: 8888,

        // redirect all not found routes to index-file
        historyApiFallback: true,

        // suppress information messages
        noInfo: true,

        // show a full-screen overlay in the browser in case of errors
        overlay: true,

        // enable HMR (Hot Module Replacement). Related plugin have to be included.
        hot: true,

        // watch-feature
        watchOptions: {
            // use polling of files' changes. Required for running inside VM
            poll: true,

            // wait ms before recompile
            aggregateTimeout: 50
        },

        // proxy some urls to another
        proxy: {
            '/api': 'http://192.168.1.50:8000',
        },
    },
};
