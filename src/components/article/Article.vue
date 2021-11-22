<template>
  <div>
    <div v-if="isMyArticle">
      <button class="btn" @click="goMovie">{{ movie.title }}</button> | 
      {{ created_at }} |
      <button class="btn" @click="finishToggle">{{btnValue}}</button>
    </div>
    <div v-else-if="!isFinish">
      <button class="btn" @click="goProfile">{{ username }}</button> |
      <button class="btn" @click="goMovie">{{ movie.title }}</button> | 
      {{ position }} | {{ created_at }}
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
      position: '',
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
    this.position = this.article['created_at']
    this.created_at = this.article['created_at']
    this.isFinish = this.article['is_finished']
    if (this.isFinish) {
      this.btnValue = '다시 구하기'
    } else {
      this.btnValue = '구했다'
    }
  }
}
</script>

<style>
.btn {
  border: solid 1px;
}
</style>