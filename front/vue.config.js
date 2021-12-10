module.exports = {
    devServer: {
        host: '127.0.0.1',
        port: 8080,
        open: true,
        proxy: {//配置跨域
            '/api': {
                target: 'http://127.0.0.1:8001',//这里后台的地址，应该填写你们真实的后台接口
                ws: true,
                secure: false,//https则是ture
                changOrigin: true,//允许跨域
                pathRewrite: {
                     '^/api': ''
                }
            },
        }
    }
};