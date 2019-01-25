<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
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
import { GET_RETRIEVE_REPORT } from '@/store/mutations/report-mutation-types.js'
import { mapGetters } from 'vuex'
import RGoods from './RGoods.vue'

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
