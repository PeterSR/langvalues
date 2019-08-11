import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import './main.css'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false


// The App itself
import App from './App.vue'

new Vue({
  render: h => h(App),
}).$mount('#root')
