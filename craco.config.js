const path = require(`path`);

// Loaders
const sassResourcesLoader = require('craco-sass-resources-loader');

const alias = (prefix) => ({
    '@app': `${prefix}/app`,
    '@common': `${prefix}/common`,
    '@components': `${prefix}/components`,
    '@pages': `${prefix}/pages`,
    '@slices': `${prefix}/slices`,
    '@utils': `${prefix}/utils`,
});
const aliases = alias(`./src`);

const resolvedAliases = Object.fromEntries(
    Object.entries(aliases).map(([key, value]) => [key, path.resolve(__dirname, value)]),
);

module.exports = {
    webpack: {
        extensions: ['', '.js', '.jsx'],
        alias: resolvedAliases,
    },
    plugins: [
        {
            plugin: sassResourcesLoader,
            options: {
                resources: './src/scss/index.scss',
            },
        },
    ],
}
