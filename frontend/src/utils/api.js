import http from './http';

const api_root = process.env.VUE_APP_API ? process.env.VUE_APP_API.replace(/\/+$/, "") : ""

class API {
    langs() {
        return http.get(api_root + "/api/langs")
    }

    values() {
        return http.get(api_root + "/api/values")
    }
}

export const api = new API()