module.exports = {
    devServer: {
        proxy: {
            "/api/*": {
                target: "http://localhost:8001/api",
                secure: false
            }
        }
    }
};
