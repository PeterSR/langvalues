<template>
    <div>
        <b-container>
            <h1>Programming Languages and their Core Values</h1>

            <b-button 
                variant="outline-primary" 
                class="lang-btn" 
                v-for="lang in langs" 
                v-bind:key="lang.id"
                v-on:click="highlight = (highlight ? null : lang)"
            >{{lang.name}}</b-button>

            <hr />

            <b-row>
                <b-col v-for="(col, index) in value_columns" v-bind:key="index">
                    <p v-for="value in col" v-bind:key="value.id">
                        <b-button variant="outline-secondary" :disabled="isDisabled(value)">{{value.name}}</b-button>
                    </p>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
import axios from "axios";

function columns(items, num_columns) {
    const num_per_column = items.length / num_columns
    var cols = []
    var newest_column = []
    for (var i = 0; i < items.length; i++) {
        newest_column.push(items[i])
        if (newest_column.length >= num_per_column) {
            cols.push(newest_column)
            newest_column = []
        }
    }
    return cols
}

export default {
    data() {
        return {
            langs: [],
            values: [],
            highlight: null,
        }
    },
    computed: {
        lang_columns: function() {
            return columns(this.langs, 3)
        },
        value_columns: function() {
            return columns(this.values, 3)
        },
    },
    methods: {
        isDisabled: function(value) {
            if (this.highlight === null) {
                return true
            }

            return !this.highlight.values.includes(value.id)
        },
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
.lang-btn {
    margin: 0.5em;
}
</style>
