<template>
  <nav class="col-lg-2 col-md-2 d-none d-lg-block d-md-block bg-light sidebar">
    <div class="sidebar-sticky">
      <!--
      <div class="about-user">
        <div class="user-photo">
          <img src="./img/user.png" alt="UserPhoto" class="mx-auto" width="100px" height="100px">
        </div>
        <div class="user-info mx-auto">
          <p class="user-info-item"><span>{{ user.first_name }}</span></p>
          <p class="user-info-item"><span>{{ user.last_name }}</span></p>
        </div>
        </div>-->
      <ul class="nav flex-column">
        <li class="nav-item">
          <router-link to="/dashboard/home" class="nav-link">Головна</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/goods" class="nav-link">Товари</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/staff" class="nav-link">Персонал</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/reports" class="nav-link">Звіти</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/settings" class="nav-link">Налаштування</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>

export default {
  name: 'Sidebar'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  padding: 56px 0 0;
  margin-bottom: 40px;
}

.sidebar-sticky {
  position: webkit-sticky;
  position: sticky;
  top: 0;
  height: calc(100vh - 56px);
  padding-top: .5em;
  overflow-x: hidden;
  overflow-y: auto;
}

.nav {
  padding-top: 1.5em;
}

.nav-link {
  text-align: left!important;
  padding-left: 3em;
  color: black;
}

.about-user {
  padding-top: 1.5em;
  width: 100%;
  height: auto;
}

.user-info {
  padding-top: 1.5em;
}

.user-info-item {
  padding: .25em;
  margin: 0;
}

</style>
