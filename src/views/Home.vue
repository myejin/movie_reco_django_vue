<template>

<div class="bg">
    <router-link :to="{name: 'Home'}">
     <img width="100" class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>

    <div style="position:relative;">
      <weather></weather>
      <weather-movie></weather-movie>
    </div>

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
</style>