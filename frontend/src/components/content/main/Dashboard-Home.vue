<template>
  <main role="main" class="col-lg-10 col-md-10 ml-sm-auto px-4">
    <h2 class="title">Головна</h2>
    <!-- <h4>#{{ report.name }}</h4> -->
    <table class="table table-bordered">
      <thead class="thead-dark">
        <tr>
          <th scope="col">#</th>
          <th scope="col">Торгова точка</th>
          <th scope="col">Час початку</th>
          <th scope="col">Час закінчення</th>
          <th scope="col">Час роботи</th>
          <th scope="col">Відсоток наявності товару</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(route, index) in report.routes" :key=route.id>
          <th scope="row">{{ index+1 }}</th>
          <td>{{ route.name }}</td>
          <td>{{ route.t_start }}</td>
          <td>{{ route.t_finish }}</td>
          <td>{{ route.t_delta }}</td>
          <td :class="'table-'+cellBackground(route.goods_status)">{{ route.goods_status }}</td>
        </tr>
      </tbody>
    </table>
    <div class='chart'>
      <canvas id="planet-chart"></canvas>
    </div>
    <div class="chart">
      <canvas id="pie-chart"></canvas>
    </div>
  </main>
</template>

<script>
import { mapGetters } from 'vuex'
import Chart from 'chart.js'
import barChartData from '@/chart/bar.js'
import doughnutChartData from '@/chart/doughnut.js'

export default{
  name: 'Main',
  data () {
    return {
      barChartData: barChartData,
      doughnutChartData: doughnutChartData
    }
  },
  computed: mapGetters(['report']),
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
    createBarChart: function (chartId, chartData) {
      const ctx = document.getElementById(chartId)
      // eslint-disable-next-line
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      })
    },
    createDoughnutChart: function (chartId, chartData) {
      const ctx = document.getElementById(chartId)
      // eslint-disable-next-line
      const myChart = new Chart(ctx, {
        type: chartData.type,
        data: chartData.data,
        options: chartData.options
      })
    }
  },
  mounted () {
    this.createBarChart('planet-chart', this.barChartData)
    this.createDoughnutChart('pie-chart', this.doughnutChartData)
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
