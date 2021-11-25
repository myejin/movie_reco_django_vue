<template>
  <div style="display:flex; justify-content:center; margin-top:1rem;">
    
    <v-text-field
      style="width:13rem;"
      label="영화 제목을 입력하세요."
      v-model.trim="inputData"
      @keyup.enter="search"
    ></v-text-field>
    <v-btn icon @click="search">
        <v-icon>mdi-magnify</v-icon>
    </v-btn>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SearchMovie',
  data: function () {
    return {
      inputData: '',
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
    search: function () {
      if (this.inputData.length) {
        axios({
          method: 'get',
          url: `${this.$defaultUrl}/movies/${this.inputData}/`,  
          headers: this.setHeader()
        })
        .then(res => {
          if ('status_code' in res.data && res.data['status_code'] === 404) {
            alert('영화를 찾을 수 없어요.')
          } else {
            this.$router.push({ name: 'MovieDetail', params: { movieId: res.data['id'] }})
          }
        })
      }
    }
  }
}
</script>

<style>

</style>