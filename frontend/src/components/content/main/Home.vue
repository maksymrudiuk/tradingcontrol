<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="content-title">Головна</h2>
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
    <p>Звіти за {{ selectedDayRange.name }}</p>
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
          <td :class="'table-'+cellBackground(report.assortment_percent)">{{ report.assortment_percent }}</td>
          <td>{{ report.owner.first_name }} {{ report.owner.last_name }}</td>
          <td>{{ report.created_at.split('T').join('-/-').slice(0, 21) }}</td>
        </tr>
      </tbody>
    </table>
    <google-map v-bind:dateRange="selectedDayRange"></google-map>
  </main>
</template>

<script>
// Chart imports
import barChartOptions from '@/chart/bar.js'
import pieChartOptions from '@/chart/pie.js'
// Components imports
import GoogleMap from './map/GoogleMap.vue'
import BarChart from './charts/BarChart.vue'
import PieChart from './charts/PieChart.vue'
// Store imports
import { mapGetters } from 'vuex'
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'

export default {
  name: 'Home',

  components: {
    BarChart,
    PieChart,
    'google-map': GoogleMap
  },

  data () {
    return {
      barOptions: barChartOptions,
      pieOptions: pieChartOptions,
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
.action-items {

}

.chart {
  width: 100%;
  height: auto;
  margin-top: 2em;
  margin-bottom: 2em;
}

.action-link {
  color: black;
  outline: none;
}

.table-bordered {
  border: 1px solid black!important;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0
}

.btn:focus {
  outline: none!important;
  box-shadow: none!important;
}
</style>
