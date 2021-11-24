<template>
  <div style="margin: 2rem 0;">
    <h2>{{ myName }}님이 좋아하는 {{ genreName }} 영화</h2>
    <v-row style="margin: 1rem 0;">
      <movie-card v-for="movie of randomMovies"
        :key="movie.id"
        :id="movie.id"
        :title="movie.title"
        :posterPath="movie.poster_path"
         style="margin: 0.2rem;"
      ></movie-card>
    </v-row>
  </div>
</template>

<script>
import MovieCard from '@/components/genremovies/MovieCard.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'GenreMovieItem',
  components: {
    MovieCard,
  },
  props: {
    genreId: Number,
  },
  data: function () {
    return {
      genreName: '',
      randomMovies: [],
    }
  },
  methods: {
    getMovies: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/genres/${this.genreId}/movies/`,
      })
      .then(res => {
        this.genreName = res.data['genre_name']
        if (res.data['movies'].length > 10) {
          this.randomMovies = _.sampleSize(res.data['movies'], 10)
        } else {
          this.randomMovies = res.data['movies']
        }
      })
    } 
  },
  computed: {
    myName: function () {
      return localStorage.getItem('myName')
    }
  },
  created: function () {
    this.getMovies()
  }
}
</script>

<style>

</style>