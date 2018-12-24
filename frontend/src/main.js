import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// eslint-disable-next-line
import Chart from 'chart.js'
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false

const token = localStorage.getItem('user-token')

if (token) {
  axios.defaults.headers.common['Authorization'] = 'JWT ' + token
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
