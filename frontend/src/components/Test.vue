<template>
    <div>
        <div v-for="lang in langs">
            <b>{{lang.name}}</b>
        </div>
        <br />
        <div v-for="value in values">
            <b>{{value.name}}</b>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            langs: [],
            values: [],
        }
    },
    mounted() {
        axios.get("/api/langs").then((response) => {
            this.langs = response.data
        }).catch((err) => {
            console.error(err)
        })

        axios.get("/api/values").then((response) => {
            this.values = response.data
        }).catch((err) => {
            console.error(err)
        })
    },
};
</script>

<style scoped>
</style>
