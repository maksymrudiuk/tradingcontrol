<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title" >Мій Персонал</h2>
    <br>
    <table v-if='isDirector' class="table table-bordered">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Ім'я</th>
          <th scope="col">Прізвище</th>
          <th scope="col">Логін</th>
          <th scope="col">Посада</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(employee, index) in getStaff" :key=employee.id>
          <th scope="row">{{ index+1 }}</th>
          <td>{{ employee.first_name }}</td>
          <td>{{ employee.last_name }}</td>
          <td>{{ employee.username }}</td>
          <td>{{ employee.role }}</td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<script>
// Store imports
import { mapGetters } from 'vuex'
import { GET_STAFF } from '@/store/mutations/user-mutation-types.js'

export default{
  name: 'Staff',

  computed: {
    ...mapGetters(['getStaff', 'isDirector'])
  },

  beforeMount () {
    this.$store.dispatch(GET_STAFF)
  }
}
</script>

<style scoped>

</style>
