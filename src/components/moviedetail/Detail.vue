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
      axios({
        method: 'post',
        url: `${this.$defaultUrl}/articles/`,  
        headers: this.setHeader(),
        data: {
          "movie_pk": 1, // movieID 가져와야해, 일단 하드코딩
          "position": '아직 위치 없음'  // gps api 사용해야해
        }
      })
      .then(() => {
        alert('게시글이 등록되었어요.')
        this.$router.push({name:'Community'})
      })
    }
  }
}
</script>

<style scoped>
.center-position {
  display:flex; 
  justify-content:center;
}

</style>