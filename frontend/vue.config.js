const path = require('path')

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? 'https://trading-control.tk/'
    : '/',
  outputDir: path.resolve(__dirname, './dist'),
  assetsDir: './assets'
}
