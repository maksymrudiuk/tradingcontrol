const path = require("path");

module.exports = {
  baseUrl: process.env.NODE_ENV === 'production'
    ? '/'
    : '/',
  outputDir: path.resolve(__dirname, "./dist"),
  assetsDir: './assets'
}
