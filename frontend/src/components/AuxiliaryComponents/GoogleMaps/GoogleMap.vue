<template>
  <div class="map-container">
    <div class="map-filter">
      <div class="row">
        <div class="col-lg-12"><h3>Фільтр</h3></div>
      </div>
      <div class="row">
        <form class="form-inline">
          <button
            type="button"
            class="btn btn-warning filter-item"
            @click="setFullDateRange()">
            За весь доступний період
          </button>
          <date-picker
            placeholder="Оберіть потрібну дату"
            class="date-picker filter-item"
            :language="uk"
            :disabledDates="disabledDates"
            v-model="selectedDate">
          </date-picker>
          <select v-if="isDirector" name="staff" id="staff" v-model="agent" class="form-control">
            <option value="" disabled selected>--Оберіть агента--</option>
            <option :value="'__all__'">Всі агенти</option>
            <option
              v-for="(agent, index) in getStaff"
              :key="index"
              :value="agent.username">
              {{ agent.first_name }}&nbsp;{{ agent.last_name }}
            </option>
          </select>
        </form>
      </div>
    </div>
    <gmap-map
      :center="center"
      :zoom="zoom"
      style="width:100%;  height: 400px;">
      <gmap-marker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        :title="m.title"
        @click="center=m.position">
      </gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
// Modules imports
import moment from 'moment'
import Datepicker from 'vuejs-datepicker'
import { en, uk } from 'vuejs-datepicker/dist/locale'
// Store imports
import { mapGetters } from 'vuex'
import { GET_STAFF } from '@/store/mutations/user-mutation-types.js'

export default {
  name: 'GoogleMap',

  components: {
    'date-picker': Datepicker
  },

  props: ['dateRange'],

  data () {
    return {
      // Map data
      center: { lat: 50.4238844, lng: 30.5655873 },
      zoom: 10,
      en: en,
      uk: uk,
      selectedDate: '__all__',
      // Agent selection
      agent: '__all__'
    }
  },

  computed: {
    ...mapGetters(['getStaff', 'getReports', 'isDirector']),
    disabledDates: function () {
      const disabledDates = {}
      let timeAgo = moment().subtract(this.dateRange, 'days').format()
      disabledDates['to'] = new Date(timeAgo)
      disabledDates['from'] = new Date()
      return disabledDates
    },
    markers: function () {
      const markers = []
      const reports = this.getReports
      if (this.selectedDate && this.agent) {
        for (let item in reports) {
          const position = {}
          const title = reports[item].store.name
          const owner = reports[item].owner.username
          const date = reports[item].created_at.split('T')[0]
          position['lat'] = reports[item].store.lat
          position['lng'] = reports[item].store.lon
          markers.push({ position, title, owner, date })
        }
      }
      var result = this.byAgent(markers, this.agent)
      result = this.byDate(result, this.selectedDate)
      return result
    }
  },

  methods: {
    // receives a place object via the autocomplete component
    setFullDateRange () {
      this.selectedDate = '__all__'
    },
    dateFormatter (date) {
      return moment(date).format('YYYY-MM-DD')
    },
    byDate (markers, date) {
      const result = []
      if (date === '__all__') {
        return markers
      } else {
        for (let m in markers) {
          if (this.dateFormatter(date) === markers[m].date) {
            result.push(markers[m])
          }
        }
        // console.log(result)
        return result
      }
    },
    byAgent (markers, agent) {
      const result = []
      if (agent === '__all__') {
        return markers
      } else {
        for (let m in markers) {
          if (agent === markers[m].owner) {
            result.push(markers[m])
          }
        }
        // console.log(result)
        return result
      }
    },
    geolocate: function () {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        }
      })
    }
  },

  mounted () {
    this.geolocate()
  },

  beforeMount () {
    this.$store.dispatch(GET_STAFF)
  }
}
</script>

<style scoped>
.map-container {
  margin: 1em!important;
}

.map-filter {
  margin: 1em;
}

.date-picker,
.date-picker>div {
  display: inline-block!important;
}

.filter-item {
  margin-left: 1em;
  margin-right: 1em;
}

.btn:focus {
  outline: none!important;
  box-shadow: none!important;
}
</style>
