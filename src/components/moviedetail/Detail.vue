<template>
  <div style="text-align:center;">
      <div >
        <img height="400px" :src="'https://image.tmdb.org/t/p/original/' + posterPath" :alt="title">
      </div>

      <div>
        <div class="title-style ">{{ title }}</div>
        <img width="80%" src="@/assets/detail_title.png" alt="">
      </div>

      <rate
        :rank="rank"
      ></rate>
      <wish :title="title"></wish>

      <div>
        <h3>장르</h3>
        <span v-for="genre of genres" :key="genre.id">
          <a @click="goGenreMovies(genre.id)" style="color: black">{{ genre.name }}</a>
          &nbsp;
        </span>
      </div>
      <div style="margin: 50px 200px" >
        <h3>줄거리</h3>
        {{ overview }}
      </div>

      <div>
        <button @click="createArticle">영화메이트 구하기</button>
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
import Rate from '@/components/moviedetail/Rate'
import Wish from '@/components/moviedetail/Wish'
import axios from 'axios'

export default {
  name:'Detail',
  components:{
    Rate,
    Wish
  },
  data: function () {
    return {
      title: '',
      overview: '',
      posterPath: '',
      genres: [],
      rank: 0,
      actors: [],
      pos: {},
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
        this.title = res.data['title']
        this.posterPath = res.data['poster_path']
        this.overview = res.data['overview']
        this.genres = res.data['genres']
        this.rank = Math.round(res.data['rank_sum'] / res.data['rank_count'] * 10) / 10
        this.actors = res.data['actors']
      })
    },
    createArticle: function () {
      if (this.pos !== 'err') {
        axios({
          method: 'post',
          url: `${this.$defaultUrl}/articles/`,  
          headers: this.setHeader(),
          data: {
            'movie_pk': this.$route.params.movieId,
            'latitude': this.pos.latitude,
            'longitude': this.pos.longitude
          }
        })
        .then(() => {
          alert('메이트 모집글이 등록되었어요.')
          this.$router.push({name:'Community'})
        })
      }
    },
    getPosition: function () {
      if('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(position => {
          this.pos = position.coords
        }, err => {
          alert(`위치정보를 받아오는 데 에러가 발생합니다.\n${err}`)
        })
      } else {
        alert('위치정보를 사용할 수 없습니다.')
      }
    },
    goGenreMovies: function (genreId) {
      this.$router.push({ name: 'GenreMovies', params: { genreId: genreId }})
    }
  },
  created: function () {
    this.getMovie()
    this.getPosition()
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

.title-style {
  font-size:50px; 
  font-weight:800;
  margin-top: 30px;
}
</style>