import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// eslint-disable-next-line
import Chart from 'chart.js'
import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDYNv60ip5q9janMxWQ8WKQYXtvgUSTR4I',
    libraries: 'places'
  }
})

const token = localStorage.getItem('user-token')

if (token) {
  axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
