<template>
  <div style="margin: 1rem 0;">
    <div v-if="userCount === 0">
      <p>많은 평점을 매길수록 많은 추천을 해드릴 수 있어요!</p>
    </div>
    <div v-else>
      <h2>{{ myName }}님과 유사한 패턴을 가진 분들</h2>
      <user-item v-for="user of similarUser"
        :key="user.user_id"
        :user="user"
      >
      </user-item>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserItem from './UserItem.vue'

export default {
  name: 'SimilarUser',
  components: {
    UserItem,
  },
  data: function () {
    return {
      similarUser: [],
      userCount: 0,
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
    getSimilarUser: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/accounts/similar/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.similarUser = res.data['users']
        this.userCount = res.data['count']
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
    }
  },
  created: function () {
    this.getSimilarUser()
  },
}
</script>

<style>

</style>