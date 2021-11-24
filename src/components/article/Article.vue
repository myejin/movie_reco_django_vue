<template>
  <tbody @click="showDetail">
    <td class="text-center" @click="goMovie">{{ username }}</td>
    <td class="text-center" @click="goProfile">{{ movie.title }}</td>
    <td class="text-center"><button class="btn" @click="goChat">채팅하기</button></td>
    <td class="text-center" v-if="show">{{ created_at }}</td>
    <td class="text-center" v-if="show">{{ address }}</td>
    <td v-if="show && isMyArticle"><button class="btn" @click="finishToggle">{{btnValue}}</button></td>
  </tbody>
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
      address: '',
      created_at: '',
      isFinish: undefined,
      btnValue: '',
      show: false,
    }
  },
  methods: {
    initMap: function () {
      console.log(window.kakao.maps.services)
    },
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
      if (!this.address.length) {
        const geocoder = new kakao.maps.services.Geocoder()
        const callback = (res, status) => {
          if (status === kakao.maps.services.Status.OK) {
            this.address = res[0]['address_name']
            console.log(this.address);
          } else {
            console.log('실패');
          }
        }
        geocoder.coord2RegionCode(this.article['longitude'], this.article['latitude'], callback)
      }
    },
    showDetail: function () {
      this.show = !this.show
      this.getAddress()
      this.$emit('show-toggle')
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
    script.onload = () => kakao.maps.load(this.initMap)
    script.type = "text/javascript"
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${process.env.VUE_APP_KAKAO_API_KEY}&libraries=services&autoload=false`
    document.head.appendChild(script)
  },
}
</script>

<style>
.btn {
  border: solid 1px;
}
</style>