module.exports = {
  lintOnSave: false, // 关闭eslint
  configureWebpack: config => {
    config.devtool = 'source-map'
  }
}
