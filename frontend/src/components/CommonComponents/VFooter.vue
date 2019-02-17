<template>
  <footer class="row footer">
    <div class="col-lg-12">
      <p class="copyright-info">&copy; Copyrights <b>Trading Control</b> 2018 - {{ currentYear }}</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'VFooter',
  data () {
    return {
      currentYear: (new Date()).getFullYear()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  z-index:          9998;
  width:            100%;
  height:           auto;
  min-height:       40px;
  position:         relative;
  background-color: #2D3035;
  color:            white;
  margin:           0;
  bottom:           0;
}

.copyright-info {
  padding: 5px;
  margin:  0;
}
</style>
