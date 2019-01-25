<template>
  <div class="card col-lg-2 my-card">
    <img class="card-img-top" :src="mediaUrl+goods.goods_item.image" :alt="goods.goods_item.name" height="100px">
    <div class="card-body">
      <h5 class="card-title">{{ goods.goods_item.name }}</h5>
      <footer class="card-text">
        <img v-if="goods.status" :src="`/static/ok.svg`" alt="Ok" width="40px">
        <img v-if="!goods.status" :src="`/static/error.svg`" alt="No" width="40px">
      </footer>
    </div>
  </div>
</template>

<script>
export default{
  name: 'RGoods',
  props: ['goods'],
  data () {
    return {
      mediaUrl: 'http://127.0.0.1:8000'
    }
  }
}
</script>

<style scoped>
.my-card {
  margin: 2em .5em;
}
</style>
