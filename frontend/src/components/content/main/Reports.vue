<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">Звіти</h2>
    <div class="btn-group" role="group" aria-label="Report Data Range">
      <button
        v-for="(item, index) in daysButtons"
        :key="index"
        type="button"
        class="btn btn-warning"
        @click="changeReportsDateRange(item.button.value, item.button.name)">
        {{ item.button.name }}
      </button>
    </div>
    <div class="row r-cards">
      <r-card
        v-for="(item, key) in getReports"
        :key="key"
        :title="item.store.name" :message="item.store.address" :id="item.id"></r-card>
    </div>
  </main>
</template>

<script>
// Components imports
import RCard from './gallery/RCard.vue'
// Store imports
import { mapGetters } from 'vuex'
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'

export default{
  name: 'Reports',

  data () {
    return {
      daysButtons: [{
        button: {
          name: '1 день',
          value: 1
        }
      }, {
        button: {
          name: '1 тиждень',
          value: 7
        }
      }, {
        button: {
          name: '2 тижні',
          value: 14
        }
      }, {
        button: {
          name: '1 місяць',
          value: 31
        }
      }],
      selectedDayRange: {
        name: '2 тижні',
        value: 14
      }
    }
  },

  components: {
    'r-card': RCard
  },

  computed: {
    ...mapGetters(['getReports'])
  },

  methods: {
    changeReportsDateRange: function (value, name) {
      // Set selected value to display
      this.selectedDayRange.name = name
      this.selectedDayRange.value = value
      // Send request again with new params
      this.$store.dispatch(GET_REPORTS, value)
    }
  },

  beforeMount () {
    this.$store.dispatch(GET_REPORTS, this.selectedDayRange.value)
  }
}
</script>

<style scoped>
.r-cards {
  margin: 0 auto;
}
</style>
