<template>
  <div>
    <div v-if="!profile.likeGenres.length && finish === false">
      <h2>좋아하는 장르가 뭔가요?</h2>
      <v-btn v-for="genre of genres"
        :key="genre.id"
        @click="addLikeGenres(genre.id)"
      >
      {{ genre.name }}
      </v-btn>
      <button @click="saveGenreList">선택완료</button>
    </div>
  </div>
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
    }
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