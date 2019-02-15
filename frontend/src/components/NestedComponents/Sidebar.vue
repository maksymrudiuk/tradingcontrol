<template>
  <nav class="col-lg-2 col-md-2 col-sm-1 bg-light sidebar">
    <div class="sidebar-sticky">
      <ul class="nav flex-column">
        <li class="nav-item">
          <router-link to="/dashboard/home" class="nav-link">
            <span class="link-icon">
              <img :src="`/static/home.svg`" alt="" width="20" height="20">
            </span>
            <a>Головна</a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/goods" class="nav-link" v-if="isDirector">
            <span class="link-icon">
              <img :src="`/static/icecream.svg`" alt="" width="20" height="20">
            </span>
            <a>Товари</a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/staff" class="nav-link" v-if="isDirector">
            <span class="link-icon">
              <img :src="`/static/staff.svg`" alt="" width="20" height="20">
            </span>
            <a>Персонал</a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/reports" class="nav-link">
            <span class="link-icon">
              <img :src="`/static/analysis.svg`" alt="" width="20" height="20">
            </span>
            <a>Звіти</a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard/settings" class="nav-link">
            <span class="link-icon">
              <img :src="`/static/controls.svg`" alt="" width="20" height="20">
            </span>
            <a>Налаштування</a>
          </router-link>
        </li>
        <li v-if="isAuthenticated" @click="showModal = true" class="nav-link">
          <span class="link-icon">
            <img :src="`/static/logout.svg`" alt="" width="20" height="20">
          </span>
          <span class="logout">Вийти</span>
        </li>
      </ul>
    </div>
    <modal v-if="showModal" @close="showModal = false"></modal>
  </nav>
</template>

<script>
// Components imports
import ExitConfirm from '../AuxiliaryComponents/ModalWindows/Modal.vue'
// Store imports
import { mapGetters } from 'vuex'

export default {
  name: 'Sidebar',

  components: {
    modal: ExitConfirm
  },

  data () {
    return {
      showModal: false,
      baseUrl: process.env.BASE_URL
    }
  },

  computed: {
    ...mapGetters(['isDirector', 'isAuthenticated'])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.link-icon {
  margin-left:  10px;
  margin-right: 10px;
}

.sidebar {
  position: fixed;
  top:      0;
  bottom:   0;
  left:     0;
  z-index:  100;
  padding:  56px 0 56px;
  height:   100vh;
}

.sidebar-sticky {
  position:    webkit-sticky;
  position:    sticky;
  top:         0;
  height:      100%;
  padding-top: .5em;
  overflow-x:  hidden;
  overflow-y:  auto;
}

.nav {
  padding-top: 1.5em;
}

.nav-link {
  text-align:   left!important;
  padding-left: 1em;
  color:        black;
  cursor:       pointer!important;
  font-size:    1em;
}

.nav-link:hover {
  color: #FFC800;
}

.about-user {
  padding-top: 1.5em;
  width:       100%;
  height:      auto;
}

.user-info {
  padding-top: 1.5em;
}

.user-info-item {
  padding: .25em;
  margin:  0;
}
</style>
