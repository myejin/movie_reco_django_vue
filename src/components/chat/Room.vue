<template>
  <div>
    <span class="bg"></span>
    <v-app id="inspire">
      <v-container class="justify-center">
        <h2>{{ toUsername }}</h2>
        <div class="messages">
          <message v-for="(data, idx) in chatLog" 
            :key="idx"
            :data="data"
          >
          </message>
        </div>
        <div class="d-flex" style="margin: 0.5rem 0;">
          <v-text-field
            label=""
            filled
            @keyup.enter="sendMessage"
            v-model.trim="inputData"
          ></v-text-field>
          <v-btn x-large @click="sendMessage" style="margin: 0.2rem;">SEND</v-btn>
        </div>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'
import Message from './Message.vue'

export default {
  components: { 
    Message, 
  },
  name: 'Room',
  data: function () {
    return {
      roomname: '',
      toUsername: '',
      chatLog: [],
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
    initSetting: function () {
      this.toUsername = this.$route.params.username 
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/chat/${this.toUsername}/room/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.roomname = res.data.room_name
        const msgList = res.data.messages
        msgList.forEach(msg => {
          this.chatLog.push(`${msg['from_user']['username']}\n${msg['content']}\n${msg['created_at']}`)
        })
        this.connect()
      })
      .catch(err => {
        if (err.response['status'] === 404) {
          console.log(err.response['status']);
          axios({
            method: 'post',
            url: `${this.$defaultUrl}/chat/${this.toUsername}/room/`,
            headers: this.setHeader()
          })
          .then(res => {
            this.roomname = res.data.room_name
            this.connect()
          })
        }
      })
    },
    alarm: function (sound, from) {
      const myName = localStorage.getItem('myName')
      if (from !== myName) {
        const audio = new Audio(sound)
        audio.play()
      }
    },
    connect: function () {
      this.socket = new WebSocket(`${this.$webSockettUrl}/${this.roomname}/`)
      this.socket.onmessage = ({ data }) => {
        const jsonData = JSON.parse(data)
        const datetime = new Date(new Date() + 3240 * 10000).toISOString().replace("T", " ").replace(/\..*/, '');
        this.chatLog.push(`${jsonData.from}\n${jsonData.message}\n${datetime}`)
        this.alarm('http://soundbible.com/mp3/Air Plane Ding-SoundBible.com-496729130.mp3', jsonData.from)
      }
      this.socket.onerror = (err) => {
        console.log(err)
        this.socket.close() 
      }
      this.socket.onclose = (err) => {
        console.log('소켓 재연결 시도중..', err.reason)
        setTimeout(() => {
          this.socket = new WebSocket(`${this.$webSockettUrl}/${this.roomname}/`)
        }, 1000);
      }
    },
    sendMessage: function () {
      if (this.inputData) {
        const myName = localStorage.getItem('myName')
        const jsonData = JSON.stringify({ 'from': myName, 'message': this.inputData })
        this.socket.send(jsonData)
        axios({
          method: 'post',
          url: `${this.$defaultUrl}/chat/${this.toUsername}/`,
          headers: this.setHeader(),
          data: {
            'content': this.inputData,
          }
        })
        this.inputData = ''
      }
    },
  },
  created: function () {
    this.initSetting()
    window.addEventListener("unload", function () {
      if(this.socket.readyState == WebSocket.OPEN) {
        this.socket.close()
      }
    })
  },
}
</script>

<style>
#inspire {
  background: none;
}
.input {
  border: solid;
  width: 450px; 
  margin: 0.3rem 0;
}
.messages {
  background-color: white;
  height: 350px;
  padding: 1rem;
  overflow: scroll;
}
</style>
