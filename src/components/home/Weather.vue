<template>
  <div >
    <img class="img-size" src="../../assets/rain.jpg" alt="">
    <!-- <img :src="weatherIcon" alt=""> -->
    <p>{{seoulWeather.data.weather[0].main}}</p>
  
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

export default {
  name:'Weather',
  computed: {
    ...mapState(['seoulWeather']),
    ...mapGetters(['weatherIcon'])
  }
}
</script>

<style scoped>
.img-size {
  position:absolute;
  margin: 0px 200px;
  height: 800px;
}
</style>