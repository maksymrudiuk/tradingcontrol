<template>
  <nav class="navbar navbar-light navbar-expand-lg sticky-top" style="background-color: #292D32;">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
      <div class="row collapse navbar-collapse" id="navbarText">
        <div class="col-lg-2">
          <router-link to="/" class="navbar-brand nav-logo">Trading Control</router-link>
        </div>
        <div class="col-lg-3 offset-lg-3 active-user">
          <p v-if="isProfileLoaded && isAuthenticated" class="username">Доброго дня,&nbsp;&nbsp;<strong>{{ getProfile.first_name }}</strong></p>
        </div>
        <div class="col-lg-2 offset-lg-2 tabs">
          <ul class="navbar-nav navbar-tips">
            <li v-if="!isAuthenticated && !authLoading && !isLoginPage" class="nav-item active nav-tip">
              <router-link to="/sign-in" class="nav-link">Увійти</router-link>
            </li>
          </ul>
        </div>
    </div>

  </nav>
</template>

<script>
import { mapGetters, mapState } from 'vuex'
import { USER_REQUEST } from '@/store/mutations/user-mutation-types.js'

export default {
  name: 'Navigation',
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters(['getProfile', 'isAuthenticated', 'isProfileLoaded']),
    ...mapState({
      authLoading: state => state.auth.status === 'loading'
    }),
    isLoginPage: function () {
      return this.$route.path === '/sign-in'
    }
  },
  beforeMount () {
    if (this.isAuthenticated) { this.$store.dispatch(USER_REQUEST) }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.active-user {
  color: white;
  float: left;
  line-height: 40px;
}

.username {
  min-height: 40px;
  margin: 0;
}

.nav-link,
.nav-logo {
  color: white!important;
  cursor: pointer;
}

.nav-link {
  padding: 2px!important;
}

.nav-logo {
  float: left;
}

.nav-tip {
  margin: 0 8px 0;
}

.nav-tip:hover {
  /* text-decoration: underline; */
  border-bottom: 1px solid white;
}

.navbar-tips {
  float: right;
}

</style>
