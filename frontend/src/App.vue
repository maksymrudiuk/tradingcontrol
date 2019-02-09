<template>
  <div id="app">
    <v-header></v-header>
    <router-view></router-view>
    <v-footer></v-footer>
  </div>
</template>

<script>
// Modules imports
import axios from 'axios'
// Components imports
import VHeader from '@/components/CommonComponents/VHeader.vue'
import VFooter from '@/components/CommonComponents/VFooter.vue'
// Store imports
import { AUTH_LOGOUT } from '@/store/mutations/auth-mutation-types.js'

export default {
  name: 'app',

  components: {
    'v-header': VHeader,
    'v-footer': VFooter
  },

  created: function () {
    axios.interceptors.response.use(undefined, function (err) {
      return new Promise(function (resolve, reject) {
        if (err.status === 401 && err.config && !err.config.__isRetryRequest) {
          this.$store.dispatch(AUTH_LOGOUT)
        }
        throw err
      })
    })
  }
}
</script>

<style>
#app {
  font-family: 'Source Sans Pro', sans-serif;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}
</style>
