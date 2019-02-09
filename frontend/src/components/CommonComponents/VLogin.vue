<template>
  <div class="center-inside">
    <form
      class="sign-in-form col-lg-4 offset-lg-4 col-md-4 offset-md-4 col-sm-8 offset-sm-2"
      @submit.prevent="login">
      <h3>Login</h3>
      <div v-if="isError" class="alert alert-danger" role="alert">
        Помилка аутентифікації
      </div>
      <div class="form-group">
        <input required v-model="username" type="text" class="form-control" id="username" placeholder="username" autocomplete="username">
      </div>
      <div class="form-group">
        <input required v-model="password" type="password" class="form-control" id="password" placeholder="password" autocomplete="current-password">
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
// Store imports
import { AUTH_REQUEST } from '@/store/mutations/auth-mutation-types.js'

export default {
  name: 'VLogin',

  data () {
    return {
      username: '',
      password: ''
    }
  },

  computed: {
    isError: function () {
      return this.$store.getters.authStatus === 'error'
    }
  },

  methods: {
    login: function () {
      const { username, password } = this
      this.$store.dispatch(AUTH_REQUEST, { username, password }).then(() => {
        // Redirect to Home page in Dashboard
        this.$router.push('/dashboard/home')
      })
    }
  }
}
</script>

<style scoped>
*, ::after, ::before {
    box-sizing: border-box;
}

.center-inside {
  display: flex;
  background-color: #f8f9fa;
  width: 100%;
  min-height: calc(100vh - 96px);
  margin: auto;
  text-align: center!important;
}

.sign-in-form {
  width: 100%;
  margin: auto;
  padding: 20px;
}

form{
  display: block!important;
}
</style>
