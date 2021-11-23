<template>
  <div style="margin: 1rem 0;">
    <h3>
      <router-link :to="{name: 'Profile', params: { username: username }}">
        {{ username }}
      </router-link>
      님이 본 영화
    </h3>  
    <v-row no-gutters>
      <v-card
        v-for="movie of rateMovies"
        :key="movie.movie_id"
        width="250"
        height="175"
        style="margin: 0 0.5rem;"
      >
        <router-link :to="{name: 'MovieDetail', params: { movieId: movie.movie_id }}">
          <v-img
            class="white--text align-end"
            :src="'https://image.tmdb.org/t/p/original/' + movie.movie_detail.poster_path"
            width="250"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          >
          </v-img>
          <v-card-title class="cardTitle">
            <v-spacer />
            <div class="cardTitle">{{ movie.movie_detail.title }}</div>
            <v-spacer />
          </v-card-title>
        </router-link>
      </v-card>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'UserItem',
  props: {
    user: Object,
  },
  data: function () {
    return {
      username: '',
      rateMovies: [],
    }
  },
  computed: {
    movieDetail: function (movieId) {

      return movieId
    }
  },
  created: function () {
    this.username = this.user.username
    this.rateMovies = this.user.rate_movies
  }
}
</script>

<style>
.cardTitle {
  padding: 0;
  font-size: 1em; 
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
</style>