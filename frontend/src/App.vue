<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view></router-view>
    <MyFooter></MyFooter>
  </div>
</template>

<script>
import Navigation from './components/navigation/Navigation.vue'
import Footer from './components/footer/Footer.vue'

export default {
  name: 'app',
  components: {
    Navigation,
    'MyFooter': Footer
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
