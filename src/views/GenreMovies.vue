<template>
  <div>
    <span class="bg"></span>
    <v-app id="inspire">
      <v-container >
        <div v-if="!genreMovies.length" style="margin: 3rem;">
          <p>{{ genreName }} 영화는 아직 없어요.</p>
        </div>

        <div v-else >
          <v-row justify="space-around">
            <v-col
              cols="12"
            >
              <v-sheet
                elevation="10"
                class="py-4 px-1"
              >
              <p class="genre-font" style="margin: 1rem;">{{ genreName }}</p>
                <v-chip-group
                  mandatory
                  active-class="primary--text"
                >
                  <v-chip
                    v-for="genre in genres"
                    :key="genre.id"
                  >
                    <router-link style="text-decoration:none; color:black;" :to="{name: 'GenreMovies', params:{genreId:genre.id}}">
                    {{ genre.name }}
                    </router-link>
                  </v-chip>
                </v-chip-group>
                <div class="moviecards">
                  <movie-card
                  v-for="movie in genreMovies"
                  :key="movie.id"
                  :id="movie.id"
                  :title="movie.title"
                  :posterPath="movie.poster_path"
                  style="margin: 0.3rem;"
                ></movie-card>
                </div>
              </v-sheet>
            </v-col>
          </v-row>
        
                  
        
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
      genres: [],
    }
  },
  methods: {
    LoadGenreMovies: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/genres/${this.$route.params.genreId}/movies/`,
      })
      .then(res => {
        console.log(res)
        this.genreName = res.data['genre_name']
        this.genreMovies = res.data['movies']
      })
    },
    getGenres: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/genres/`,
      })
      .then(res => {
        console.log(res.data,'!!');
        this.genres = res.data['genres']
      })
    },
  },
  created: function () {
    if ('jwt' in localStorage) {
      this.LoadGenreMovies()
    } else {
      this.$router.push({ name: 'Home'})
    }
    this.getGenres()
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