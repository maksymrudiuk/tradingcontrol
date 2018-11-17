<template>
  <div class="center-inside">
    <form class="sign-in-form" @submit.prevent="login">
      <h3>Login</h3>
      <div class="form-group">
        <!-- <label for="username">Username</label> -->
        <input required v-model="username" type="text" class="form-control" id="username" placeholder="username" autocomplete="username">
      </div>
      <div class="form-group">
        <!-- <label for="password">Password</label> -->
        <input required v-model="password" type="password" class="form-control" id="password" placeholder="password" autocomplete="current-password">
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
    </form>
  </div>
</template>

<script>
import { AUTH_REQUEST } from '@/store/mutations/auth-mutation-types.js'

export default {
  name: 'Sign-in',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login: function () {
      const { username, password } = this
      this.$store.dispatch(AUTH_REQUEST, { username, password }).then(() => {
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
  max-width: 30%;
  margin: auto;
  padding: 20px;
}

form{
  display: block!important;
}
</style>
