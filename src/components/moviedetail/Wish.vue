<template>
  <div class="my-3">
    <v-btn @click="addWishList">{{ btnValue }}</v-btn>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'

export default {
  name:'Wish',
  props: {
    title: String,
  },
  data: function () {
    return {
      btnValue: '',
      state: false,
    }
  },
  methods:{
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    addWishList: function() {
      axios({
        method:'post',
        url:`${this.$defaultUrl}/movies/${this.$route.params.movieId}/wish/`,
        headers: this.setHeader()
     })
     .then(() =>{
       this.state = !this.state
        if (this.state === true) {
          this.btnValue = 'nowish'
          alert('위시리스트에서 추가되었어요.')
        } else {
          this.btnValue = 'addwish'
          alert('위시리스트에 삭제되었어요.')
        }
     })
    }
  },
  computed: {
    ...mapState([
      'profile',
    ]),
  },
  created: function () {
    for (let movie of this.profile.wishMovies) {
      if (movie['title'] === this.title) {
        this.state = true
        break 
      }
    }
    if (this.state === true) {
      this.btnValue = 'nowish'
    } else {
      this.btnValue = 'addwish'
    }
  }
}
</script>

<style>

</style>