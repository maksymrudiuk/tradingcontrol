<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">{{ retrieveReport.store.name }}</h2>
    <p><strong>{{ retrieveReport.store.address }}</strong><p>
    <div class="row">
      <r-goods
        v-for="(item, key) in retrieveReport.assortment"
        :key="key"
        :goods="item">
      </r-goods>
    </div>
  </main>
</template>

<script>
// Components imports
import RGoods from './RGoods.vue'
// Store imports
import { mapGetters } from 'vuex'
import { GET_RETRIEVE_REPORT } from '@/store/mutations/report-mutation-types.js'

export default{
  name: 'RAlbum',
  props: ['reportId'],

  components: {
    'r-goods': RGoods
  },

  computed: {
    ...mapGetters(['retrieveReport'])
  },

  beforeMount () {
    console.log(this.reportId)
    this.$store.dispatch(GET_RETRIEVE_REPORT, this.reportId)
  }
}
</script>

<style scoped>
</style>
