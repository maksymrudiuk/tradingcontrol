<template>
  <div class="card col-lg-3 my-card" :class="hightligthCards()">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">{{ address }}</p>
      <p class="card-text">{{ dateOfCreate }}</p>
      <div>
<!--         <router-link
          class="btn btn-light"
          :to="{ name: 'reportDetails', params: { reportId: id, address: address, title: title }}">
          Детально
        </router-link> -->
        <router-link
          class="btn btn-light"
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
  props: ['title', 'address', 'id', 'reportCreatedDate', 'percent'],
  data () {
    return {
      threshold: 40
    }
  },

  computed: {
    dateOfCreate: function () {
      return this.reportCreatedDate.split('T')[0]
    }
  },

  methods: {
    hightligthCards: function () {
      if (this.percent >= this.threshold) {
        return 'card-success'
      } else {
        return 'card-warning'
      }
    }
  }
}
</script>

<style scoped>
.my-card {
  margin: 2em .5em;
}
.card-success {
  background-color: rgba(63, 191, 63, 0.6)
}
.card-warning {
  background-color: rgba(222, 204, 37, 0.6)
}
</style>
