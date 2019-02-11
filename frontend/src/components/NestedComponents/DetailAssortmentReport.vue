<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">{{ title }}</h2>
    <p><strong>{{ address }}</strong><p>
    <div class="row">
      <r-goods
        v-for="(item, key) in retrieveReport.assortment"
        :key="key+1"
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
  name: 'DetailAssortmentReport',
  props: ['reportId', 'title', 'address'],

  components: {
    'r-goods': RGoods
  },

  computed: {
    ...mapGetters(['retrieveReport'])
  },

  mounted () {
    this.$store.dispatch(GET_RETRIEVE_REPORT, this.reportId)
  }
}
</script>

<style scoped>
</style>
