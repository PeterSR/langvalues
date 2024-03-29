<template>
    <div>
        <b-container>
            <h1 class="title">LangValues <img :src="require('../assets/logo.png')"/></h1>
            <h2 class="subtitle">Programming Languages and their Core Values</h2>

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

            <p class="core-footer">Don't see your favorite language or value on the list? Disagreeing with some values? <a href="mailto:langvalues@petersr.com">Get in touch</a> or <a href="https://github.com/PeterSR/langvalues/issues">open an issue</a>.</p>
        </b-container>
    </div>
</template>

<script>
import {api} from "../utils/api"

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
        api.data().then((data) => {
            if (!data) {
                throw new Error("Invalid data.")
            }

            if (data.langs) {
                this.langs = data.langs
                this.langs.sort((a, b) => (a.name < b.name ? -1 : 1))
            }

            if (data.values) {
                this.values = data.values
                this.values.sort((a, b) => (a.name < b.name ? -1 : 1))
            }
        }).catch((err) => {
            console.error(err)
        })
    },
};
</script>

<style scoped>
.title img {
    width: 1.3em;
    height: auto;
}

.subtitle {
    color: gray;
    font-size: 0.9em;
}

.lang-nav {
    margin: 2em auto;
}

.value {
    font-size: 2em;
    line-height: 2.3em;
    color: gray;
}

.value.highlighted {
    color: orange;
}

.core-footer {
    margin-top: 2em;
    font-size: 0.8em;
    color: gray;
    text-align: center;
}
</style>
