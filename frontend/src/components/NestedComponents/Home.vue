<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">Головна</h2>
    <c-date-selector @clicked="onClickChild" ></c-date-selector>
    <div class="chart">
      <bar-chart
        :chartdata='getBarDatacollection'
        :options='barOptions'
        :height='600'>
      </bar-chart>
    </div>
    <div class="chart">
      <pie-chart
        :chartdata='getPieDatacollection'
        :options='pieOptions'
        :height='400'>
      </pie-chart>
    </div>
    <table class="table table-bordered table-sm">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Торгова точка</th>
          <th scope="col">Час початку</th>
          <th scope="col">Час закінчення</th>
          <th scope="col">Тривалість роботи</th>
          <th scope="col">Відсоток наявності товару</th>
          <th scope="col">Власник</th>
          <th scope="col">Cтворений</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(report, index) in getReports" :key=report.id>
          <th scope="row">{{ index+1 }}</th>
          <td>{{ report.store.name }}</td>
          <td>{{ report.t_start }}</td>
          <td>{{ report.t_finish }}</td>
          <td>{{ report.t_delta }}</td>
          <td
            :class="'table-'+cellBackground(report.assortment_percent)">
            <router-link
              class='action-link'
              :to="{ name: 'reportDetails',
                     params: {
                        reportId: report.id,
                        address: report.store.address,
                        title: report.store.name
                      }
                    }">
          {{ report.assortment_percent }}
        </router-link>
          </td>
          <td>{{ report.owner.first_name }} {{ report.owner.last_name }}</td>
          <td>{{ report.created_at.split('T').join('-/-').slice(0, 21) }}</td>
        </tr>
      </tbody>
    </table>
    <google-map :dateRange="forDays"></google-map>
  </main>
</template>

<script>
// Chart imports
import barChartOptions from '@/chart/bar.js'
import pieChartOptions from '@/chart/pie.js'
// Components imports
import GoogleMap from '../AuxiliaryComponents/GoogleMaps/GoogleMap.vue'
import BarChart from '../AuxiliaryComponents/Charts/BarChart.vue'
import PieChart from '../AuxiliaryComponents/Charts/PieChart.vue'
import CommonDateSelector from '../AuxiliaryComponents/DateSelectors/CommonDateSelector.vue'
// Store imports
import { mapGetters } from 'vuex'
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'
import getCookie from '@/utils/cookies.js'

export default {
  name: 'Home',

  components: {
    BarChart,
    PieChart,
    'google-map': GoogleMap,
    'c-date-selector': CommonDateSelector
  },

  data () {
    return {
      barOptions: barChartOptions,
      pieOptions: pieChartOptions,
      forDays: getCookie('forDays') || 14
    }
  },

  computed: {
    ...mapGetters(['reportStatus', 'getReports', 'getBarDatacollection', 'getPieDatacollection'])
  },

  methods: {
    cellBackground: function (value) {
      if (value >= 70) {
        return 'success'
      } else if (value < 70 & value >= 40) {
        return 'warning'
      } else {
        return 'danger'
      }
    },
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
.chart {
  width:         100%;
  height:        auto;
  margin-top:    2em;
  margin-bottom: 2em;
}

.action-link {
  color:   black;
  outline: none!important;
}

.table-bordered {
  border: 1px solid black!important;
}

.btn:focus {
  outline:    none!important;
  box-shadow: none!important;
}
</style>
