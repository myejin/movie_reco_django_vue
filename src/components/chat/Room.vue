<template>
  <div>
    <textarea class="border-1" :value="chatLog" cols="50" rows="20"></textarea><br>
    <input class="border-1" @keyup.enter="sendMessage" v-model="inputData" type="text" size="44">
    <button class="border-1" @click="sendMessage">Send</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000' // store 로 보내기

export default {
  name: 'Room',
  data: function () {
    return {
      roomname: '',
      toUsername: '',
      chatLog: '',
      inputData: '',
    }
  },
  methods: {
    initSetting: function () {
      this.toUsername = this.$route.params.username 
      axios({
        method: 'get',
        url: `${SERVER_URL}/chat/${this.toUsername}/room/`,  
        headers: {
          'Authorization': 'JWT 토큰하드코딩!!!'
        }
      })
      .then(res => {
        this.roomname = res.data.room_name
        const msgList = res.data.messages
        msgList.forEach(msg => {
          this.chatLog += `${msg['from_user']['username']} : ${msg['content']} (${msg['created_at']})\n`
        })
        this.connect()
      })
      .catch(err => {
        if (err.response['status'] === 404) {
          console.log(err.response['status']);
          axios({
            method: 'post',
            url: `${SERVER_URL}/chat/${this.toUsername}/room/`,
            headers: {
              'Authorization': 'JWT 토큰하드코딩!!!'
            }
          })
          .then(res => {
            this.roomname = res.data.room_name
            this.connect()
          })
        }
      })
    },
    connect: function () {
      if (this.socket === undefined || this.socket.readyState === 3) {
        this.socket = new WebSocket(`ws://localhost:8000/ws/chat/${this.roomname}/`)
        this.socket.onmessage = ({ data }) => {
          const jsonData = JSON.parse(data)
          const datetime = new Date(+new Date() + 3240 * 10000).toISOString().replace("T", " ").replace(/\..*/, '');
          this.chatLog += (`username? : ${jsonData.message} (${datetime})\n`) // 로그인 후 유저네임 store에 저장
        }
      }
    },
    sendMessage: function () {
      const jsonData = JSON.stringify({ 'message': this.inputData })
      this.socket.send(jsonData)
      axios({
        method: 'post',
        url: `${SERVER_URL}/chat/${this.toUsername}/`,
        headers: {
          'Authorization': 'JWT 토큰하드코딩!!!'
        },
        data: {
          'content': this.inputData,
        }
      })
      this.inputData = ''
    },
    disconnect: function () {
      if (this.socket.readyState === 1) {
        this.socket.send(JSON.stringify({ 'message': "삭제할게요" }))
        this.socket.close()
      }
    }
  },
  created: function () {
    this.initSetting()
  },
  beforeDestroy: function () {
    this.disconnect()
  }
}
</script>

<style>
.border-1 {
  border: solid;
}
</style>
