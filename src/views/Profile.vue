<template>
  <div>
    <!-- <span class="bg"></span> -->
    <v-app id="inspire">
      <v-container >
        <div class="m-2">
          <v-row>
            <h2 style="margin: 0.5rem">{{ username }}</h2>
            <v-sheet color="white" style="margin: 0.5rem; text-align: center;">
              <p>팔로워</p>
              <p>{{ profile.followerCnt }}</p>
            </v-sheet>
            <v-sheet color="white" style="margin: 0.5rem; text-align: center;">
              <p>팔로잉</p>
              <p>{{ profile.followingCnt }}</p>
            </v-sheet>
            <v-btn 
              @click="followToggle" 
              v-if="!isMyProfile"
              style="margin: 0.5rem 1rem;"
            >
              {{ followBtn }}
            </v-btn>
          </v-row>
        </div>
        <div class="m-2">
          <v-row no-gutters v-if="!show">
            <v-col>
              <h3>좋아하는 장르</h3>
              <div v-if="profile.likeGenres.length">
                <span v-for="genre of profile.likeGenres" :key="genre.id">
                  <!-- <router-link :to="{name: 'MovieDetail', params: { genreId: genre.id }}"> -->
                    {{ genre.name }}
                  <!-- </router-link> -->
                  &nbsp;
                </span>
              </div>
              <div v-else>특별히 없어요.</div>
            </v-col>
            <v-col v-if="isMyProfile"><v-btn @click="genreToggle">변경</v-btn></v-col>
          </v-row>
          <div v-else>
            <genre-choice></genre-choice>
            <v-btn @click="genreToggle" color="accent" style="margin: 0.1rem;">취소</v-btn>
          </div>
        </div>
        <div class="m-2">
          <h3>위시리스트</h3>
          <div v-if="profile.wishMovies.length">
            <v-row>
              <v-card 
                v-for="movie of profile.wishMovies"
                :key="movie.id"
                width="300"
                style="margin: 1rem;"
              >
                <router-link :to="{name: 'MovieDetail', params: { movieId: movie.id }}">
                  <v-img
                    class="white--text align-end"
                    :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
                    width="300"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  >
                  </v-img>
                  <v-card-title style="padding: 0;">
                    <v-spacer />
                    <div class="cardTitle">{{ movie.title }}</div>
                    <v-spacer />
                  </v-card-title>
                </router-link>
              </v-card>
            </v-row>
          </div>
          <div v-else>등록된 영화가 없어요.</div>
        </div>
        <div class="m-2">
          <h3>평점을 매긴 영화</h3>
          <div v-if="profile.rateMovies.length">
            <v-row>
              <v-card 
                v-for="data of profile.rateMovies"
                :key="data.movie.id"
                width="300"
                style="margin: 1rem;"
              >
                <router-link :to="{name: 'MovieDetail', params: { movieId: data.movie.id }}">
                  <v-img
                    class="white--text align-end"
                    :src="'https://image.tmdb.org/t/p/original/' + data.movie.poster_path"
                    width="300"
                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  >
                    <v-card-text style="color: white; position: absolute; bottom: 0; left: 0;">{{ data.rank }}</v-card-text>
                  </v-img>
                  <v-card-title style="padding: 0;">
                    <v-spacer />
                    <div class="cardTitle">{{ data.movie.title }}</div>
                    <v-spacer />
                  </v-card-title>
                </router-link>
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

export default {
  name:'Profile',
  components: {
    GenreChoice
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
    this.getProfile()
    this.getFollowInfo()
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
  font-size: 0.8em; 
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
</style>