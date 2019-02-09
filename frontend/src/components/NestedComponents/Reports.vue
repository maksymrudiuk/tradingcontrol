<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">Звіти</h2>
    <c-date-selector @clicked="onClickChild"></c-date-selector>
    <div class="row r-cards">
      <r-card
        v-for="(item, key) in getReports"
        :key="key"
        :title="item.store.name"
        :address="item.store.address"
        :id="item.id"
        :reportCreatedDate="item.created_at"
        :percent="item.assortment_percent"></r-card>
    </div>
  </main>
</template>

<script>
// Components imports
import RCard from './RCard.vue'
import CommonDateSelector from '../AuxiliaryComponents/DateSelectors/CommonDateSelector.vue'
// Store imports
import { mapGetters } from 'vuex'
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'

export default{
  name: 'Reports',

  components: {
    'c-date-selector': CommonDateSelector,
    'r-card': RCard
  },

  data () {
    return {
      forDays: localStorage.getItem('dateSelector')
    }
  },

  computed: {
    ...mapGetters(['getReports'])
  },

  methods: {
    onClickChild: function (value) {
      this.forDays = value
    }
  },

  beforeMount () {
    this.$store.dispatch(GET_REPORTS, this.forDays)
  }
}
</script>

<style scoped>
.r-cards {
  margin: 0 auto;
}
</style>
