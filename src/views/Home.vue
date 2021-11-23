<template>
  <div>
    <span class="bg"></span>
      <v-app id="inspire">
        <v-container >
          <v-row >
          

            <v-col  sm="0" lg="2">
              <div style="position:relative;">
                <img class="img-size" src="../assets/rain.jpg" alt="">
                <weather></weather>
                <weather-movie></weather-movie>
              </div>
            </v-col>
          
          </v-row>
        </v-container>
      </v-app>
    
    <router-link :to="{name: 'Home'}">
     <img width="100" class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>
    <similar-user></similar-user>
  </div>
</template>


<script>
import WeatherMovie from '../components/home/WeatherMovie.vue'
import Weather from '../components/home/Weather.vue'
import SimilarUser from '../components/home/SimilarUser.vue'

export default {
  name: 'Home',
  components:{
    WeatherMovie,
    Weather,
    SimilarUser,
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