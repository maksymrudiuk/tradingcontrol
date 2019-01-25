<template>
  <div class="container-fluid content">
    <div class="row">
      <Sidebar></Sidebar>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from './nav/Sidebar.vue'

export default {
  name: 'Content',
  components: {
    Sidebar
  }
}
</script>

<style scoped>
.content {
  width: 100%;
  min-height: calc(100vh - 96px);
}
</style>

<style>
.content-title {
  margin-top: 1em;
  margin-bottom: 1em;
}
</style>
