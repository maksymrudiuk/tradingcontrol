<script>
// Vue - chart lib imports
import { Bar } from 'vue-chartjs'
// My utils imports
import getColor from '@/utils/colors.js'

export default {
  extends: Bar,

  props: {
    chartdata: {
      type: Object,
      default: null
    },
    colors: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },

  methods: {
    colorify: function (chartdata) {
      const backgroundColor = []
      const borderColor = []
      let data = chartdata.datasets[0].data

      for (let item in data) {
        let color = getColor(data[item])
        backgroundColor.push(color.rgba)
        borderColor.push(color.rgb)
      }

      chartdata.datasets[0]['backgroundColor'] = backgroundColor
      chartdata.datasets[0]['borderColor'] = borderColor
    }
  },

  mounted () {
    this.colorify(this.chartdata)
    this.renderChart(this.chartdata, this.options)
  },

  watch: {
    chartdata: {
      handler: function (val, oldval) {
        this.colorify(this.chartdata)
        this.renderChart(val, this.options)
      }
    }
  }
}
</script>

<style>
</style>
