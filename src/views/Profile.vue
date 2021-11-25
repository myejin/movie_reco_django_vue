<template>
  <div>
    <span class="bg"></span>
    <v-app id="inspire">
      <v-container >
        <div class="m-2" style="text-align: center;">
            <div style="margin: 1rem; font-size:5rem;">{{ username }}</div>

            <div style="display:flex; justify-content:center; font-weight:1000;">
            <div style="margin: 0.5rem; text-align: center; background: none; ">
              <p>팔로워</p>
              <p>{{ profile.followerCnt }}</p>
            </div>
            <div style="margin: 0.5rem; text-align: center; background: none;">
              <p>팔로잉</p>
              <p>{{ profile.followingCnt }}</p>
            </div>
            </div>

            <v-btn 
              @click="followToggle" 
              v-if="!isMyProfile"
              style="margin: 0.5rem 1rem;"
            >
              {{ followBtn }}
            </v-btn>
          
        </div>
        <div class="m-2">
          <v-row no-gutters v-if="!show">
            <v-col style="text-align:center;">
              <h3>좋아하는 장르</h3>
              <div v-if="profile.likeGenres.length">
                <v-chip
                  v-for="genre of profile.likeGenres"
                  :key="genre.id"
                  @click="addLikeGenres(genre.id)"
                >
                  <router-link style="text-decoration:none" :to="{name: 'GenreMovies', params: { genreId: genre.id }}">
                  <span style="color: black;">{{ genre.name }}</span>
                  </router-link>
                </v-chip>
              </div>
              <div v-else></div>
              <v-col v-if="isMyProfile"><v-btn @click="genreToggle">선택</v-btn></v-col>
            </v-col>
          </v-row>
          <div v-else style="text-align:center;">
            
            <genre-choice></genre-choice>
            <v-btn @click="genreToggle" color="grey" style="margin: 0.1rem; color: white;">취소</v-btn>

          </div>
        </div>
        <div class="m-2">
          <h3>위시리스트</h3>
          <div v-if="profile.wishMovies.length" style="margin: 1rem 0;">
            <v-row>
              <movie-card v-for="movie of profile.wishMovies"
                :key="movie.id"
                :id="movie.id"
                :title="movie.title"
                :posterPath="movie.poster_path"
                style="margin: 0.2rem;"
              ></movie-card>
            </v-row>
          </div>
          <div v-else>등록된 영화가 없어요.</div>
        </div>
        <div class="m-2">
          <h3>평점을 매긴 영화</h3>
          <div v-if="profile.rateMovies.length" style="margin: 1rem 0;">
            <v-row>
              <v-card v-for="data of profile.rateMovies"
                :key="data.movie.id"
                class="mx-1 my-1"
                max-width="344"
                @click="goDetail(data.movie.id)"
              >
                <v-img
                  :src="`https://image.tmdb.org/t/p/original${data.movie.poster_path}`"
                  height="200px"
                >
                  <v-card-text style="color: white; position: absolute; bottom: 0; left: 0;">{{ data.rank }}</v-card-text>
                </v-img>

                <v-card-title class="cardTitle">
                  {{data.movie.title}}
                </v-card-title>

                <v-card-actions>
                  <v-btn
                    color="orange lighten-2"
                    text
                  >
                    DETAIL
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-row>
          </div>
          <div v-else>아직 없어요.</div>
        </div>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'
import GenreChoice from '../components/home/GenreChoice.vue'
import MovieCard from '../components/genremovies/MovieCard.vue'

export default {
  name:'Profile',
  components: {
    GenreChoice,
    MovieCard,
  },
  data: function () {
    return {
      profile: {
        likeGenres: [],
        rateMovies: [],
        wishMovies: [],
        followerCnt: 0,
        followingCnt: 0,
        followerList: [],
      },
      isFollow: false,
      followBtn: '',
      show: false,
    }
  },
  methods: {
    goDetail: function (movieId) {
        this.$router.push({name: 'MovieDetail', params: { movieId: movieId }})
    },
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    getProfile: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/accounts/${this.username}/profile/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.profile.likeGenres = res.data['like_genres']
        this.profile.rateMovies = res.data['rate_movies']
        this.profile.wishMovies = res.data['wish_movies']
      })
    },
    getFollowInfo: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/accounts/${this.username}/follow/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.profile.followerCnt = res.data['follower_count']
        this.profile.followingCnt = res.data['following_count']
        this.profile.followerList = res.data['follower_list']

        const myName = localStorage.getItem('myName')
        let exist = false 
        for (let follower of res.data['follower_list']) {
          if (follower.username === myName) {
            exist = true 
            break
          }
        }
        if (exist) {
          this.isFollow = true
          this.followBtn = '팔로우 취소'
        } else {
          this.followBtn = '팔로우'
        }
      })
    },
    followToggle: function () {
      axios({
        method: 'post',
        url: `${this.$defaultUrl}/accounts/${this.username}/follow/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.profile.followerCnt = res.data['follower_count']
        this.isFollow = !this.isFollow
        if (this.isFollow) {
          this.followBtn = '팔로우 취소'
        } else {
          this.followBtn = '팔로우'
        }
      })
    },
    getSrc: function (posterPath) {
      return `https://image.tmdb.org/t/p/original/${posterPath}`
    },
    genreToggle: function () {
      this.show = !this.show
    }
  },
  computed: {
    username: function () {
      return this.$route.params.username
    },
    isMyProfile: function () {
      return this.username === localStorage.getItem('myName')
    }
  },
  created: function () {
    if ('jwt' in localStorage) {
      this.getProfile()
      this.getFollowInfo()
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

.m-2 {
  margin: 2rem 0 0 2rem;
}
.cardTitle {
  padding: 1rem;
  font-size: 25px;
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
  
}
</style>