<template>
  <div class="mt-16">
    <links></links>
    <div class="center-position">
      <img height="400px" :src="'https://image.tmdb.org/t/p/original/' + posterPath" :alt="title">

      <div class="ms-16">
        <h1>{{ title }}</h1>
        <img width="80%" src="@/assets/detail_title.png" alt="">
      </div>
      <!-- 혜진추가 -->
      <div>평점 : {{ rank }}</div>
      <div>
        <h3>장르</h3>
        <span v-for="genre of genres" :key="genre.id">{{ genre.name }}&nbsp;</span>
      </div>
      <div>
        <h3>줄거리</h3>
        {{ overview }}
      </div>
    </div>
    <!-- actor -->
    <div class="bg">
      <v-slide-group
        class="pa-4 mx-auto"
        style="width:75%;"
      >
        <v-slide-item
          v-for="actor in actors"
          :key="actor.id"
        > 
          <v-card
            class="ma-4"
            height="250"
            width="150"
          >
            <img width="100%" height="200" 
              :src="'https://image.tmdb.org/t/p/original/' + actor.profile_path" 
              :alt="actor.name"
            >
            <v-card-title style="padding: 0;">
              <v-spacer />
              <div class="actorName">{{ actor.name }}</div>
              <v-spacer />
            </v-card-title>
          </v-card>
        </v-slide-item>
      </v-slide-group>
    </div>
  </div>
</template>

<script>
import Links from '@/components/moviedetail/Links'
import axios from 'axios'

export default {
  name:'Detail',
  components: {
    Links
  },
  data: function () {
    return {
      title: '',
      overview: '',
      posterPath: '',
      genres: [],
      rank: 0,
      actors: [],
    }
  },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    getMovie: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/movies/${this.$route.params.movieId}/`,  
        headers: this.setHeader()
      })
      .then(res => {
        console.log( res.data['actors']);
        this.title = res.data['title']
        this.posterPath = res.data['poster_path']
        this.overview = res.data['overview']
        this.genres = res.data['genres']
        this.rank = Math.round(res.data['rank_sum'] / res.data['rank_count'] * 10) / 10
        this.actors = res.data['actors']
      })
    }
  },
  created: function () {
    this.getMovie()
  }
}
</script>

<style scoped>
.center-position {
  display:flex; 
  justify-content:center;
}
.actorName {
  font-size: 0.8em; 
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
</style>