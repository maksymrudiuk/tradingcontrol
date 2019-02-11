<template>
  <div class="container-fluid content">
    <div class="row">
      <Sidebar></Sidebar>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// Components imports
import Sidebar from '../NestedComponents/Sidebar.vue'

export default {
  name: 'VContainer',
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
