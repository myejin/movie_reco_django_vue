<template>
  <div class="weather-position">
    
    <div style="margin-top:180px;">
      <p class="font-style1" >{{seoulWeather.main}}</p>
      <p class="font-style2" >{{seoulWeather.description}}</p>
    </div>

    <div class="center-position">
      <img style="width: 200px;" :src="isIcon" alt="">
      <p class="font-style1">Seoul</p>
      <p class="font-style2">{{nowTemp}} °C</p>
    </div>

    <div style="text-align: right; margin-top:160px;" >
      <p  class="font-style2">11-23</p>
      <p  class="font-style2">20:57</p>
      <p  class="font-style2">{{minTemp}} °C / {{maxTemp}} °C</p>
    </div>
  
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

export default {
  name:'Weather',
  computed: {
    ...mapState(['seoulWeather','addWeatherData']),
    ...mapGetters(['nowTemp','maxTemp','minTemp']),
    isIcon: function () {
      if (this.seoulWeather.icon) {
        return `http://openweathermap.org/img/wn/${this.seoulWeather.icon}@2x.png`
      } else {
        return ''
      }
    },
  },
}
</script>

<style scoped>
.weather-position {
  position: absolute;
  width: 1000px;
  top:120px;
  left: 170px;
  display: flex;
  justify-self: space-around;
}
.center-position {
  text-align: center; 
  margin:0px 130px; 
}
.font-style1 {
  color: white;
  font-size: 60px;
  margin-bottom: 0;
}
.font-style2 {
  color: white;
  font-size: 40px;
  margin-bottom: 0;
}
</style>