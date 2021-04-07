module.exports = {
    purge: {
        // change to `true` to force turning on
        //
        // it's useful to disable it during development -
        // you will be able to see all possible styles in dev-tool
        enabled: false,
        content: [
            './src/**/*.html',
            './src/**/*.js',
        ]
    },
    darkMode: false,
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
};
