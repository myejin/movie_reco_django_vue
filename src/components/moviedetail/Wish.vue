<template>
  <div class="my-3">
    <v-btn @click="addWishList">addwish</v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'Wish',

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
     .then(res =>{
       console.log(res)
     })
    }
  }
}
</script>

<style>

</style>