<template>
  <div class="btn-group" role="group" aria-label="Report Data Range">
    <button
      v-for="(item) in daysButtons"
      :key="item.id"
      :id="`btn-` + item.button.id"
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
import getCookie from '@/utils/cookies.js'

export default {
  name: 'CommonDateSelector',

  data () {
    return {
      daysButtons: [{
        button: {
          id: 1,
          name: '1 день',
          value: 1
        }
      }, {
        button: {
          id: 2,
          name: '1 тиждень',
          value: 7
        }
      }, {
        button: {
          id: 3,
          name: '2 тижні',
          value: 14
        }
      }, {
        button: {
          id: 4,
          name: '1 місяць',
          value: 31
        }
      }],

      forDays: getCookie('forDays') || 14

    }
  },

  methods: {
    changeDateRange: function (value) {
      this.forDays = value
      this.$emit('clicked', value)
      this.$store.dispatch(GET_REPORTS, this.forDays)
      document.cookie = 'forDays=' + value
      this.dellClassFromElements('btn-selected') // It`s terrible
    },
    checkDate: function (value) {
      if (value === this.forDays) {
        return 'btn-selected'
      }
    },
    // It`s terrible
    markSelectedDate: function () {
      var savedVal = parseInt(getCookie('forDays'))
      for (let key in this.daysButtons) {
        if (savedVal === this.daysButtons[key].button.value) {
          var id = 'btn-' + this.daysButtons[key].button.id
          this.setClassToElementById(id, 'btn-selected')
        }
      }
    },
    // It`s terrible
    setClassToElementById: function (id, className) {
      var element = document.getElementById(id)
      element.classList.add(className)
    },
    // It`s terrible
    dellClassFromElements: function (className) {
      const elements = document.getElementsByClassName(className)
      if (elements.length !== 0) {
        elements[0].classList.remove(className)
      } else {
        return null
      }
    }
  },

  mounted () {
    this.markSelectedDate()
  }
}
</script>

<style>
.btn-selected {
  color:            #212529;
  background-color: #e0a800;
  border-color:     #d39e00;
}
.btn:focus {
  outline:    none!important;
  box-shadow: none!important;
}
</style>
