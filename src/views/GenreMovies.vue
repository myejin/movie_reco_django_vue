<template>
  <div>
    <p class="genre-font">{{genreMovies.genre_name}}</p>
    <div class="moviecards">
      <movie-card
        v-for="movie in genreMovies.movies"
        :key="movie.id"
        :movie="movie"
      ></movie-card>
    </div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import MovieCard from '@/components/genremovies/MovieCard'
export default {
  name:'GenreMovies',
  components:{
    MovieCard
  },
  created: function() {
    this.$store.dispatch('LoadGenreMovies')
  },
  computed: {
    ...mapState(['genreMovies'])
  }
}
</script>

<style scoped>
.moviecards {
  display:flex; 
  justify-content:center;
   flex-wrap: wrap;
}
.genre-font{
  font-size: 50px;
  text-align: center;
}
</style>