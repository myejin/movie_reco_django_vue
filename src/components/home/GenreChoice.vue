<template>
  <span v-if="finish === false">
    <h2 style="text-align:center; margin-bottom:2rem;">장르를 선택하세요.</h2>
    <v-row>
      <v-col
        
      >
        <!-- <v-sheet
          elevation="10"
          class="py-4 px-1"
        > -->
          <v-chip-group
            multiple
            active-class="primary--text"
          >
            <v-chip
              v-for="genre of genres"
              :key="genre.id"
              @click="addLikeGenres(genre.id)"
            >
              {{ genre.name }}
            </v-chip>
          </v-chip-group>
        <!-- </v-sheet> -->
      </v-col>
    </v-row>
    <span style="display:inline-block;" >
    <v-btn color="grey" @click="saveGenreList" style="color: white; " class="align-self-center ma-3" >저장</v-btn>
    </span>
    
  </span>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  name: 'GenreChoice',
  data: function () {
    return {
      genres: [],
      likeGenres: [],
      finish: false,
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
      if (this.myName.length) {
        axios({
          method: 'get',
          url: `${this.$defaultUrl}/accounts/${this.myName}/profile/`,  
          headers: this.setHeader()
        })
        .then(res => {
          this.$store.dispatch("setProfile", res.data)
        })
      }
    },
    getGenres: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/genres/`,
      })
      .then(res => {
        console.log(res.data);
        this.genres = res.data['genres']
      })
    },
    addLikeGenres: function (genreId) {
      if (genreId in this.likeGenres) {
        this.likeGenres.pop(genreId)
      } else {
        this.likeGenres.push(genreId)
      }
    },
    saveGenreList: function () {
      this.finish = true
      axios({
        method: 'put',
        url: `${this.$defaultUrl}/accounts/genres/`,  
        headers: this.setHeader(),
        data: {
          'genres': this.likeGenres,
        }
      })
      .then(() => {
        alert('장르가 저장되었어요!')
        this.$router.go()
      })
    },
  },
  computed: {
    ...mapState([
      'profile',
    ]),
    myName: function () {
      if ('myName' in localStorage) {
        return localStorage.getItem('myName')
      } else {
        return ''
      }
    },
  },
  created: function () {
    this.getProfile()
    this.getGenres()
  }
}
</script>

<style>
.movieName {
  font-size: 0.8em; 
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
</style>