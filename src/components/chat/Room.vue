<template>
  <div>
    <button class="border-1" @click="connect" v-if="socketDisabled === true">연결</button>
    <button class="border-1" @click="disconnect" v-if="socketDisabled === false">해제</button><br>
    <textarea class="border-1" :value="chatLog" cols="100" rows="20"></textarea><br>
    <input class="border-1" @keyup.enter="sendMessage" v-model="inputData" type="text" size="100"><br>
    <button class="border-1" @click="sendMessage" :disabled="socketDisabled === true">Send</button>
  </div>
</template>

<script>
export default {
  name: 'Room',
  data: function () {
    return {
      socketDisabled: true,
      socket: undefined,
      // logs: [],
      selected: 'json',
      chatLog: 'tmp!!!!',
      inputData: '',
    }
  },
  methods: {
    connect: function () {
      console.log('hi')
      if (this.socket === undefined || this.socket.readyState === 3) {
        this.socket = new WebSocket(`ws://localhost:8000/ws/chat/${this.$route.params.roomname}/`)
        this.socket.onopen = () => {
          this.socket.send(JSON.stringify({
            message:"hihihihi",
          }))
        }
        this.socketDisabled = false
        console.log(this.socket)
        console.log(this.socketDisabled)
        this.socket.onerror = () => {
          console.log({ type: 'ERROR', msg: 'ERROR:' })
        }
        this.socket.onmessage = (e) => {
          console.log(e)
          const data = JSON.parse(e.data)
          this.chatLog += (data.message + '\n')
          console.log({ type: 'RECV', msg: 'RECV' + e.data })
        }
        this.socket.onclose = (msg) => {
          console.log({ type: 'ERROR', msg: `Closed (Code: ${msg.code}, Message: ${msg.reason})` })
        }
      }

    },
    sendMessage: function () {
      if (this.selected === 'plain') {
        console.log({ type: 'SENT', msg: 'SENT' + this.inputData })
        this.socket.send(this.inputData)
      } else if (this.selected === 'json') {
        const tmp = JSON.stringify({ 'message':this.inputData })
        console.log({ type: 'SENT', msg: 'SENT' + JSON.stringify(tmp)})
        this.socket.send(tmp)
      }
      this.inputData = ''
    },
    disconnect () {
      if (this.socket.readyState === 1) {
        this.socket.close()
        console.log({ type: 'INFO', msg: 'DISCONNECTED' })
        this.socketDisabled = true 
      }
    }
  },
}
</script>

<style>
.border-1 {
  border: solid;
}
</style>