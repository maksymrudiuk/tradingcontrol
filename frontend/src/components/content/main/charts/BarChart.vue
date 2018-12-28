<script>
import { Bar } from 'vue-chartjs'
import rgbGenerate from '@/utils/colors.js'

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

      for (var item = 0; item <= chartdata.labels.length; item++) {
        let color = rgbGenerate()
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
        // console.log('Watcher handler')
        this.colorify(this.chartdata)
        this.renderChart(val, this.options)
      }
    }
  }
}
</script>

<style>
</style>
