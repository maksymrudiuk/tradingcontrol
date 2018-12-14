<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="title">Головна</h2>
    <!-- <h4>#{{ report.name }}</h4> -->
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
    <!-- <p>{{ getBarDatacollection }}</p> -->
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
  </main>
</template>

<script>
import { mapGetters } from 'vuex'
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'
import barChartOptions from '@/chart/bar.js'
import pieChartOptions from '@/chart/pie.js'
import BarChart from './BarChart.vue'
import PieChart from './PieChart.vue'

export default{
  name: 'Home',
  components: {
    BarChart,
    PieChart
  },
  data () {
    return {
      barOptions: barChartOptions,
      pieOptions: pieChartOptions
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
    }
  },
  mounted () {
  },
  beforeMount () {
    this.$store.dispatch(GET_REPORTS)
  }
}

</script>

<style scoped>

.title {
  margin-top: 1em;
  margin-bottom: 1em;
}

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
</style>
