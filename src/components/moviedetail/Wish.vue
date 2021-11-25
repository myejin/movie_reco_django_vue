<template>
  <div class="my-3">
    <v-btn @click="addWishList" v-if="dataBtn.length">{{ dataBtn }}</v-btn>
    <v-btn @click="addWishList" v-else>{{ btnValue }}</v-btn>
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
      dataBtn: '',
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
    getProfile: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/accounts/${this.myName}/profile/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.$store.dispatch("setProfile", res.data)
      })
    },
    addWishList: function() {
      axios({
        method:'post',
        url:`${this.$defaultUrl}/movies/${this.$route.params.movieId}/wish/`,
        headers: this.setHeader()
      })
      .then(() => {
        if (!this.dataBtn.length) {
          this.dataBtn = this.btnValue
        }
        if (this.dataBtn === 'addwish') {
          this.dataBtn = 'nowish'
          alert('위시리스트에 추가되었어요.')
        } else {
          this.dataBtn = 'addwish'
          alert('위시리스트에서 삭제되었어요.')
        }
      })
    }
  },
  computed: {
    ...mapState([
      'profile',
    ]),
    myName: function () {
      return localStorage.getItem('myName')
    },
    btnValue: function () {
      for (let movie of this.profile.wishMovies) {
        if (movie['title'] === this.title) {
          return 'nowish'
        }
      }
      return 'addwish'
    }
  },
  created: function () {
    this.getProfile()
  }
}
</script>

<style>

</style>