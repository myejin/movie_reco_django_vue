<template>

<div>
    <router-link :to="{name: 'Home'}">
     <img width="100" class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: 1} }">detail</router-link>
    <movie-card
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"
    ></movie-card>
    <weather></weather>
</div>
</template>

<script>
import MovieCard from '../components/home/MovieCard.vue'
import Weather from '../components/home/Weather.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components:{
    MovieCard,
    Weather
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
