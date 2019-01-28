<template>
  <div class="hello">
    <h1>It`s a not public app!</h1>
    <router-link
      to="/dashboard/home"
      class="nav-link">
      Головна
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Greeting'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello{
  width: 100%;
  height: calc(100vh - 96px);
}

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
