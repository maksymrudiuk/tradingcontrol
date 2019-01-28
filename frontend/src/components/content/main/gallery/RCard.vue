<template>
  <div class="card col-lg-3 my-card">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ message }}</p>
      <div>
        <router-link
          class="btn btn-primary"
          :to="{ name: 'reportDetails', params: { reportId: id }}">
          Детально
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default{
  name: 'RCard',
  props: ['title', 'message', 'id'],

  methods: {
    seeDetail: function () {
      this.$router.push('/dashboard/reports/' + this.id)
    }
  }
}
</script>

<style scoped>
.my-card {
  margin: 2em .5em;
}
</style>
