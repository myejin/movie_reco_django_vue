<template>

<div>
    <router-link :to="{name: 'Home'}">
     <img width="100" class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>

    <weather-movie
    ></weather-movie>
    <weather></weather>
</div>
</template>

<script>
import WeatherMovie from '../components/home/WeatherMovie.vue'
import Weather from '../components/home/Weather.vue'

export default {
  name: 'Home',
  components:{
    WeatherMovie,
    Weather
  },
}
</script>
