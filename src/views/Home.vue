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
</div>
</template>

<script>
import MovieCard from '../components/home/MovieCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components:{
    MovieCard
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  }
}
</script>
