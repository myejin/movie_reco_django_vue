<template>
  <div>
    <button @click="getAddress">나와라</button>
    <div v-if="isMyArticle">
      <button class="btn" @click="goMovie">{{ movie.title }}</button> | 
      {{ created_at }} |
      <button class="btn" @click="finishToggle">{{btnValue}}</button>
    </div>
    <div v-else-if="!isFinish">
      <button class="btn" @click="goProfile">{{ username }}</button> |
      <button class="btn" @click="goMovie">{{ movie.title }}</button> | 
      {{ distance }} | {{ address }} | {{ created_at }} 
      <button class="btn" @click="goChat">채팅하기</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Article',
  props: {
    article: Object,
  },
  data: function () {
    return {
      username: '',
      movie: {},
      distance: 0,
      address: '',
      created_at: '',
      isFinish: undefined,
      btnValue: '',
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
    finishToggle: function () {
      this.isFinish = !this.isFinish
      axios({
        method: 'put',
        url: `${this.$defaultUrl}/articles/${this.article['id']}/`,  
        headers: this.setHeader(),
        data: {
          'is_finished': this.isFinish
        }
      })
      .then(() => {
        if (this.isFinish) {
          this.btnValue = '다시 구하기'
        } else {
          this.btnValue = '구했다'
        }
      })
    },
    goProfile: function () {
      // this.$router.push({ name: 'Profile', params: { username: this.username } })
    },
    goMovie: function () {
      this.$router.push({ name:'MovieDetail', params: { movieId: this.movie['id'] } })
    },
    goChat: function () {
      this.$router.push({ name: 'Chat', params: { username: this.username } })
    },
    getAddress: function () {
      const geocoder = new kakao.maps.services.Geocoder()
      // const coord = new kakao.maps.LatLng(this.article['latitude'], this.article['longitude'])
      const callback = function(res, status) {
        if (status === kakao.maps.services.Status.OK) {
          alert(res)
          console.log(res);
        }
      }
      geocoder.coord2RegionCode(this.article['latitude'], this.article['longitude'], callback)
    }
  },
  computed: {
    isMyArticle: function () {
      const myName = localStorage.getItem('myName')
      if (myName === this.username) {
        return true 
      } else {
        return false 
      }
    },
  },
  created: function () {
    this.username = this.article['author']['username']
    this.movie = this.article['movie']
    this.distance = this.article['dist']
    this.created_at = this.article['created_at']
    this.isFinish = this.article['is_finished']
    if (this.isFinish) {
      this.btnValue = '다시 구하기'
    } else {
      this.btnValue = '구했다'
    }
  },
  mounted: function () {
    const script = document.createElement('script')
    /* global kakao */
    script.type = "text/javascript"
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${process.env.VUE_APP_KAKAO_API_KEY}&libraries=services&autoload=false`
    document.head.appendChild(script)
  }
}
</script>

<style>
.btn {
  border: solid 1px;
}
</style>