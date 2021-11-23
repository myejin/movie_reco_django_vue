<template>
  <div>
    <span class="bg"></span>
      <v-app id="inspire">
        <v-container >
          <v-row >
          <!-- 
            <v-col class="pt-10 my-10 pb-16">
              <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>
            </v-col> -->

            <v-col sm="0" lg="2">
              <div style="position:relative;">
                <img class="img-size" src="../assets/rain.jpg" alt="">
                <weather></weather>
                <weather-movie></weather-movie>
              </div>
            </v-col>
          
          </v-row>
        </v-container>
      </v-app>
    
  </div>
</template>

<script>
import Weather from '@/components/home/Weather'
import WeatherMovie from '@/components/home/WeatherMovie'

export default {
  name: 'Home',
  components:{
    WeatherMovie,
    Weather
  },

  created: function () {
    this.$store.dispatch('LoadWeatherMovie')
  },
}
</script>

<style scoped>
.bg {
  background-image: url('../assets/main_bg.jpg');
  background-size : 100%;
  background-repeat: repeat;
  position:absolute;
  width: 100%;
  height: 100%;
}


#inspire {
  background: none;
}
.img-size {
  width:1160px;
  margin-top: 100px;
}
</style>