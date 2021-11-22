<template>

<div>
    <router-link :to="{name: 'Home'}">
     <img width="100" class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>

    <weather></weather>
    <weather-movie></weather-movie>
    <div style="padding:2000px"></div>
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
