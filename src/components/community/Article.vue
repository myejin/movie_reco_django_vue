<template>
  <div>
    <div v-if="!article.is_finished || article.author.username === myName">
      <a @click="goProfile" class="a-align" style="width:20%; color: black;">{{ username }}</a>
      <a @click="goMovie" class="a-align" style="width:40%; color: black;">{{ movie.title }}</a>
      <a class="a-align" style="width:10%; color: black;"><span @click="showDetail">detail</span></a>
      <a class="a-align" style="width:10%; color: black;" v-if="!isMyArticle"><span @click="goChat">chat</span></a>
    </div>
    <div v-if="show" style="border: 1px solid; margin: 1rem; padding: 1rem; width:80%;">
        <div style = "display: flex; justify-content:flex-end">
          <v-btn x-small @click="showDetail">X</v-btn>
        </div>
        <div>
          <span>게시일자 : {{ created_at }}</span><br>
          <span>상세주소 : {{ address }}</span><br>
          <span>모집여부 : {{ btnValue }}</span>
          <v-btn x-small
            v-if="isMyArticle" 
            @click="finishToggle"
            style="margin: 0.5rem;"
          >
            변경
          </v-btn>
        </div>
        <br>
        <div>
          <input type="text" 
            v-model.trim="inputData" 
            placeholder="리뷰를 등록하세요"
            style="border: 2px solid; width: 85%"
            @keyup.enter="addReview"
          >
          <v-btn small @click="addReview" style="margin: 0.1rem;">작성</v-btn>
        </div>
        <br>
        <div v-if="reviews.length">
          <h4>리뷰 {{ reviews.length }}개</h4>
          <div v-for="(review, idx) of reverseReviews"
            :key="idx"
          >
            {{ review.author.username }}: {{ review.content }}
            (created at : {{ created_at }})
            <v-btn small 
              @click="delReview(review)"
              v-if="review.author.username === myName"
            >
            삭제
            </v-btn>
          </div>
        </div>
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
      address: '',
      created_at: '',
      isFinish: undefined,
      btnValue: '',
      show: false,
      reviews: [],
      inputData: '',
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
      })
      .then(() => {
        if (this.isFinish) {
          this.btnValue = '완료'
        } else {
          this.btnValue = '모집중'
        }
      })
    },
    goProfile: function () {
      this.$router.push({ name: 'Profile', params: { username: this.username } })
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
    },
    getReview: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/articles/${this.article.id}/reviews/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.reviews = res.data['reviews']
      })
    },
    addReview: function () {
      if (this.inputData.length) {
        axios({
          method: 'post',
          url: `${this.$defaultUrl}/articles/${this.article.id}/reviews/`,  
          headers: this.setHeader(),
          data: {
            'content': this.inputData,
          }
        })
        .then(res => {
          console.log(res.data);
          this.reviews.push(res.data['review'])
          this.inputData = ''
        })
      }
    },
    delReview: function (review) {
      axios({
        method: 'delete',
        url: `${this.$defaultUrl}/articles/reviews/${review.id}/`,  
        headers: this.setHeader(),
      })
      .then(() => {
        this.reviews.pop(review)
      })
    }
  },
  computed: {
    myName: function () {
      if ('myName' in localStorage) {
        return localStorage.getItem('myName')
      } else {
        return ''
      }
    },
    isMyArticle: function () {
      if (this.myName === this.username) {
        return true 
      } else {
        return false 
      }
    },
    reverseReviews: function () {
      return [...this.reviews].reverse()
    }
  },
  created: function () {
    this.username = this.article['author']['username']
    this.movie = this.article['movie']
    this.created_at = this.article['created_at']
    this.isFinish = this.article['is_finished']
    if (this.isFinish) {
      this.btnValue = '완료'
    } else {
      this.btnValue = '진행중'
    }
    this.getReview()
  },
  mounted: function () {
    const script = document.createElement('script')
    /* global kakao */
    script.onload = () => kakao.maps.load(this.initMap)
    script.type = "text/javascript"
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${process.env.VUE_APP_KAKAO_API_KEY}&libraries=services&autoload=false`
    document.head.appendChild(script)
    this.getAddress()
  },
}
</script>

<style>
.a-align {
  text-decoration: none; 
  display:inline-block; 
  text-align: center; 
}
a:hover {
  text-decoration: underline; 
}
</style>