<template>
  <div>
    <h2
      class="content-title">
      {{ retrieveReport.store }}
    </h2>
    <p>
      <strong>
        {{ retrieveReport.store }}
      </strong>
    <p>
    <hr>
    <div class="row">
      <p class="row-title">Ассортимент</p>
      <r-goods
        v-for="(item, key) in retrieveReport.assortment"
        :key="key+1"
        :goods="item">
      </r-goods>
    </div>
    <hr>
    <div class="row store-images">
      <p class="row-title">Холодильник</p>
      <div class="cold-store">
        <div v-for="(item, key) in storePhotos"
          class="img-container"
          :key="key+1">
        <img
          :src="mediaUrl+item.file"
          alt=""
          width="300px"
          class="img-store orientation-6">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Components imports
import RGoods from './RGoods.vue'
import EXIF from 'exif-js'
// Store imports
import { mapGetters } from 'vuex'
import { GET_RETRIEVE_REPORT, GET_STORE_PHOTOS } from '@/store/mutations/report-mutation-types.js'

export default{
  name: 'DetailAssortmentReport',
  props: ['reportId'],

  data () {
    return {
      mediaUrl: 'http://127.0.0.1:8000'
    }
  },

  components: {
    'r-goods': RGoods
  },

  computed: {
    ...mapGetters(['retrieveReport', 'storePhotos'])
  },

  methods: {
    checkExif: function () {
      var images = document.getElementsByClassName('img-store')
      var containers = document.getElementsByClassName('img-container')
      for (let key in images) {
        EXIF.getData(images[key], function () {
          var orientation = EXIF.getTag(this, 'Orientation')
          console.log(orientation)
          if (parseInt(orientation) === 6) {
            containers[key].classList.add('orientation-6')
          }
        })
      }
    }
  },

  mounted () {
    this.$store.dispatch(GET_RETRIEVE_REPORT, this.reportId)
    this.$store.dispatch(GET_STORE_PHOTOS, this.reportId)
    // this.checkExif()
    console.log('Mounted')
  },
}
</script>

<style scoped>
.my-card {
  margin:     2em .5em;
  min-height: 150px;
  height:     auto;
}
.store-images {
  height: auto;
}
.row-title {
  font-size:  1.5em;
  text-align: center;
  display:    block;
  height:     auto;
  width:      100%;
}
.cold-store {
  width:    100%;
  height:   auto;
}
.img-container {
  display:       inline-block;
  margin-bottom: 4em;
  margin-top:    4em;
}
.img-store {
  display:  inline-block;
  overflow: hidden;
  /* border:   5px solid green; */
}
.orientation-6 {
  transform:                rotate(90deg);
  -ms-transform:            rotate(90deg);
  -moz-transform:           rotate(90deg);
  -webkit-transform:        rotate(90deg);
  -o-transform:             rotate(90deg);
/*   -webkit-transform-origin: center;
  -moz-transform-origin:    center;
  -ms-transform-origin:     center;
  -o-transform-origin:      center;
  transform-origin:         center; */
}
</style>
