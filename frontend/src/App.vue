<template>
  <div id="app">
    <MyHeader></MyHeader>
    <router-view></router-view>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
// Modules imports
import axios from 'axios'
// Components imports
import Header from './components/header/Header.vue'
import Footer from './components/footer/Footer.vue'
// Store imports
import { AUTH_LOGOUT } from '@/store/mutations/auth-mutation-types.js'

export default {
  name: 'app',

  components: {
    'MyHeader': Header,
    'MyFooter': Footer
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
