<template>
  <div class="weather-position">
    

    <img :src="weatherIcon" alt="">
    <p class="font-style">{{seoulWeather.data.weather[0].main}}</p>
    <!-- <p class="font-style">{{seoulWeather.data.main.temp - 273.15}}</p> -->
  
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

export default {
  name:'Weather',
  computed: {
    ...mapState(['seoulWeather']),
    ...mapGetters(['weatherIcon'])
  },
}
</script>

<style scoped>
.weather-position {
  position: absolute;
  top:150px;
  left: 150px;
}
.font-style {
  color: white;
  font-size: 80px;
}
</style>