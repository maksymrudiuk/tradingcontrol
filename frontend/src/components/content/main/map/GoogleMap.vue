<template>
  <div class="map-container">
<!--     <div class="map-filter">
      <h3>Фільтр</h3>
      <date-picker
        placeholder="Оберіть бажану дату"
        class="date-picker filter-item"
        :language="uk"
        v-model="selectedDate">
      </date-picker>
      <select v-if="isDirector" name="staff" id="staff" v-model="agent">
        <option value="0" disabled selected>--Оберіть агента--</option>
        <option
          v-for="(agent, index) in getStaff"
          :key="index"
          :value="agent.username">
          {{ agent.first_name }}{{ agent.last_name }}
        </option>
      </select>
      <button type="button" class="btn btn-primary filter-item" @click="markerFilter()">Пошук</button>
    </div> -->
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
import { mapGetters } from 'vuex'
import Datepicker from 'vuejs-datepicker'
import { en, uk } from 'vuejs-datepicker/dist/locale'
import { GET_STAFF } from '@/store/mutations/user-mutation-types.js'

export default {
  name: 'GoogleMap',

  components: {
    'date-picker': Datepicker
  },

  data () {
    return {
      // change this to whatever makes sense
      center: { lat: 50.4238844, lng: 30.5655873 },
      zoom: 10,
      en: en,
      uk: uk,
      selectedDate: null,
      agent: null,
    }
  },

  computed: {
    ...mapGetters(['getStaff', 'getReports', 'isDirector']),
    markers: function () {
      const markers = []
      const reports = this.getReports
      for (var item in reports) {
        const position = {}
        const title = reports[item].store.name
        const owner = reports[item].owner.username
        const date = reports[item].created_at
        position['lat'] = reports[item].store.lat
        position['lng'] = reports[item].store.lon
        markers.push({ position, title, owner, date })
      }
      return markers
    }
  },

  methods: {
    // receives a place object via the autocomplete component
    setPlace (place) {
      this.currentPlace = place
    },
    addMarker () {
      if (this.currentPlace) {
        const marker = {
          lat: this.currentPlace.geometry.location.lat(),
          lng: this.currentPlace.geometry.location.lng()
        }
        this.markers.push({ position: marker })
        this.places.push(this.currentPlace)
        this.center = marker
        this.currentPlace = null
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
</style>
