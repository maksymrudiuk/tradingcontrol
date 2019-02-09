<template>
  <div class="btn-group" role="group" aria-label="Report Data Range">
    <button
      v-for="(item, index) in daysButtons"
      :key="index"
      type="button"
      class="btn btn-warning"
      @click="changeDateRange(item.button.value, item.button.name)">
      {{ item.button.name }}
    </button>
  </div>
</template>

<script>
import { GET_REPORTS } from '@/store/mutations/report-mutation-types.js'

export default {
  name: 'CommonDateSelector',

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

      forDays: localStorage.dateSelector
        ? localStorage.getItem('dateSelector')
        : 14
    }
  },

  methods: {
    changeDateRange: function (value, name) {
      localStorage.dateSelector = value
      this.forDays = value
      this.$emit('clicked', value)
      this.$store.dispatch(GET_REPORTS, this.forDays)
    }
  }
}
</script>

<style></style>
