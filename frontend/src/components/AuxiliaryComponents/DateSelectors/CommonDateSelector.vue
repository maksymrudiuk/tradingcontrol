<template>
  <div class="btn-group" role="group" aria-label="Report Data Range">
    <button
      v-for="(item, index) in daysButtons"
      :key="index"
      type="button"
      class="btn btn-warning"
      :class="checkDate(item.button.value)"
      @click="changeDateRange(item.button.value)">
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
    changeDateRange: function (value) {
      localStorage.dateSelector = value
      this.forDays = value
      this.$emit('clicked', value)
      this.$store.dispatch(GET_REPORTS, this.forDays)
    },
    checkDate: function (value) {
      if (value === this.forDays) {
        return 'btn-selected'
      }
    }
  }
}
</script>

<style>
.btn-selected {
  color: #212529;
  background-color: #e0a800;
  border-color: #d39e00;
}
.btn:focus {
  outline: none!important;
  box-shadow: none!important;
}
</style>
