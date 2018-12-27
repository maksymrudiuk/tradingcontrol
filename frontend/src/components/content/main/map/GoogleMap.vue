<template>
  <div class="map-container">
    <!-- <div>
      <h2>Search and add a pin</h2>
      <label>
        <gmap-autocomplete
          @place_changed="setPlace">
        </gmap-autocomplete>
        <button @click="addMarker">Add</button>
      </label>
      <br/>

    </div> -->
    <br>
    <gmap-map
      :center="center"
      :zoom="zoom"
      style="width:100%;  height: 400px;"
    >
      <gmap-marker
        :key="index"
        v-for="(m, index) in getStoreMarkers"
        :position="m.position"
        :title="m.title"
        @click="center=m.position"
      ></gmap-marker>
    </gmap-map>
    <p></p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'GoogleMap',
  data () {
    return {
      // default to Montreal to keep it simple
      // change this to whatever makes sense
      center: { lat: 50.4238844, lng: 30.5655873 },
      zoom: 10
    //   markers: [{
    //     position: {
    //       lat: 50.4238844,
    //       lng: 30.5655873
    //     }
    //   }, {
    //     position: {
    //       lat: 50.25492,
    //       lng: 28.67105
    //     }
    //   }],
    //   places: [],
    //   currentPlace: null
    // }
    }
  },

  computed: {
    ...mapGetters(['getStoreMarkers',])
  },

  mounted () {
    this.geolocate()
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
  }
}
</script>

<style scoped>
.map-container {
  margin: 1em!important;
}
</style>
