<template>
  <div style="margin: 1rem 0;">
    <h3>
      <router-link class=" text-decoration-none font-style" :to="{name: 'Profile', params: { username: username }}">
        {{ username }}
      </router-link>
        님이 본 영화
    </h3>  
  
    <v-slide-group
      show-arrows
      class="pa-4 mx-auto"
      style="width:100%;"
    >
      <v-slide-item
        v-for="movie of rateMovies"
        :key="movie.movie_id"
      >
        <v-card
          width="240"
          height="200"
          style="margin: 0 0.5rem;"
        >
          <router-link class=" text-decoration-none" :to="{name: 'MovieDetail', params: { movieId: movie.movie_id }}">
            <v-img
              class="white--text align-end"
              :src="'https://image.tmdb.org/t/p/original/' + movie.movie_detail.poster_path"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            >
            </v-img>
            <v-card-title  class="cardTitle  font-style">
              <v-spacer />
            <div class="cardTitlee">{{ movie.movie_detail.title }}</div>
              <v-spacer />
            </v-card-title>
          </router-link>
        </v-card>
      </v-slide-item>
    </v-slide-group>
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

<style scoped>
.cardTitle {
  padding: 0;
  font-size: 1em; 
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
#inspire {
  background: none;
}
.font-style {
  color:black;
  font-size: 20px;
  margin-top: 1rem;
}
</style>