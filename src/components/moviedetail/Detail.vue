<template>
  <div >
    <links></links>
    <div class="center-position">
      <img height="400px" src="@/assets/영화포스터샘플.jpg" alt="">
      
      <div class="ms-16">
        <h1>영화제목</h1>
        <img width="80%" src="@/assets/detail_title.png" alt="">

      </div>

      <div>
        <button @click="createArticle">영화메이트 구하기</button>
      </div>
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
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    createArticle: function () {
      const pos = this.getPosition()
      if (pos !== 'err') {
        axios({
          method: 'post',
          url: `${this.$defaultUrl}/articles/`,  
          headers: this.setHeader(),
          data: {
            'movie_pk': this.$route.params.movieId,
            'latitude': pos.latitude,
            'longitude': pos.longitude
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
        navigator.geolocation.getCurrentPosition(position => position.coords, err => {
          alert(`위치정보를 받아오는 데 에러가 발생합니다.\n${err}`)
          return 'err'
        })
      } else {
        alert('위치정보를 사용할 수 없습니다.')
        return 'err'
      }
    },
  }
}
</script>

<style scoped>
.center-position {
  display:flex; 
  justify-content:center;
}

</style>