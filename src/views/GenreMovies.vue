<template>
  <div>
    <span class="bg"></span>
    <v-app id="inspire">
      <v-container >
        <p class="genre-font" style="margin: 1rem;">{{ genreName }}</p>
        <div v-if="!genreMovies.length" style="margin: 3rem;">
          <p>{{ genreName }} 영화는 아직 없어요.</p>
        </div>
        <div v-else class="moviecards">
          <movie-card
            v-for="movie in genreMovies"
            :key="movie.id"
            :id="movie.id"
            :title="movie.title"
            :posterPath="movie.poster_path"
            style="margin: 0.3rem;"
          ></movie-card>
        </div>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import MovieCard from '@/components/genremovies/MovieCard'
import axios from 'axios'

export default {
  name:'GenreMovies',
  components:{
    MovieCard
  },
  data: function () {
    return {
      genreName: '',
      genreMovies: [],
    }
  },
  methods: {
    LoadGenreMovies: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/genres/${this.$route.params.genreId}/movies/`,
      })
      .then(res => {
        console.log(res.data);
        this.genreName = res.data['genre_name']
        this.genreMovies = res.data['movies']
      })
    } 
  },
  created: function () {
    if ('jwt' in localStorage) {
      this.LoadGenreMovies()
    } else {
      this.$router.push({ name: 'Home'})
    }
  }
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