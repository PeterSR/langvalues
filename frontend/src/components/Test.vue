<template>
    <div>
        <b-container>
            <h1>Programming Languages and their Core Values</h1>

            <b-button-toolbar key-nav aria-label="Languages to choose from">
                <b-button-group class="lang-nav">
                    <b-button
                        variant="outline-primary"
                        class="lang-btn btn-lg"
                        v-for="lang in langs"
                        v-bind:key="lang.id"
                        v-on:click="highlighted_lang = (highlighted_lang != lang ? lang : null)"
                        v-bind:class="{active: lang == highlighted_lang}"
                    >{{lang.name}}</b-button>
                </b-button-group>
            </b-button-toolbar>

            <hr />

            <b-row>
                <b-col v-for="(col, index) in value_columns" v-bind:key="index">
                    <ul>
                        <li class="value" v-for="value in col" v-bind:key="value.id" v-bind:class="{highlighted: highlight(value)}">
                            {{value.name}}
                        </li>
                    </ul>
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
            highlighted_lang: null,
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
        highlight: function(value) {
            return this.highlighted_lang !== null && this.highlighted_lang.values.includes(value.id)
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
h1 {
    margin: 1em 0;
}

.lang-nav {
    margin: 1em auto;
}

.value {
    font-size: 2em;
    line-height: 2.3em;
    color: gray;
}

.value.highlighted {
    color: orange;
}
</style>
