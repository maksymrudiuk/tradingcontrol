<script>
// Vue - charrt lib imports
import { Pie } from 'vue-chartjs'

export default {
  extends: Pie,

  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },

  mounted () {
    this.renderChart(this.chartdata, this.options)
  },

  watch: {
    chartdata: {
      handler: function (val, oldval) {
        this.renderChart(val, this.options)
      }
    }
  }
}
</script>

<style>
</style>
