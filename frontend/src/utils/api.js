import http from './http';
import yaml from 'js-yaml';

//const api_root = process.env.VUE_APP_API ? process.env.VUE_APP_API.replace(/\/+$/, "") : ""

class API {
    get_yaml() {
        return http.get("/assets/langvalues.yaml").then((response) => {
            return yaml.load(response.data)
        })
    }

    data() {
        return this.get_yaml().then((data) => {
            let langs = data.languages
            let values = data.values

            var values_map = values.reduce(function(obj, x) {
                obj[x.id] = x
                return obj
            }, {})

            for (let lang of langs) {
                lang.values = data.relationship.filter((rel) => {
                    return rel.lang === lang.id
                }).map((rel) => {
                    return values_map[rel.value]
                })
            }

            return {
                langs: langs,
                values: values,
            }
        })
    }
}

export const api = new API()