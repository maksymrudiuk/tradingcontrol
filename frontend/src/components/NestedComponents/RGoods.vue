<template>
  <div
    class="card col-lg-2 my-card"
    :class="setBackground()">
    <img
      class="card-img-top"
      :src="mediaUrl+goods.goods_item.image"
      :alt="goods.goods_item.name"
      height="150px">
    <div class="card-body">
      <h4 class="card-title">{{ goods.goods_item.name }}</h4>
    </div>
  </div>
</template>

<script>
export default{
  name: 'RGoods',
  props: ['goods'],

  data () {
    return {
      mediaUrl: process.env.NODE_ENV === 'production'
        ? 'https://trading-control.tk'
        : 'http://127.0.0.1:8000'
    }
  },

  methods: {
    setBackground () {
      if (this.goods.status) {
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
  margin:  2em .5em;
  padding: 1em;
}
.status-img {
  margin: 0 auto;
}
.card-success {
  background-color: rgba(63, 191, 63, 0.6)
}
.card-warning {
  background-color: rgba(222, 204, 37, 0.6)
}
</style>
