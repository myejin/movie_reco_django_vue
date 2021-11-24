<template>
  <div>
    <span class="bg"></span>
    <v-app id="inspire">
      <v-container>
        <h2>Direct Message</h2>
        <v-card v-for="room of rooms" 
          :key="room.roomname" 
          class="mx-auto"
          max-width="344"
          outlined
        >
          <v-list-item three-line>
            <v-list-item-content>
              <v-list-item-title class="text-h5 mb-1">
                {{ room.username }}
              </v-list-item-title>
              <v-list-item-subtitle>ROOM {{ room.roomname }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-card-actions>
            <v-btn
              outlined
              rounded
              text
              @click="goChat(room.username)"
            >
              CHAT
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ChatRooms',
  data: function () {
    return {
      rooms: [],
      selectUser: '',

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
    goChat: function (username) {
      this.$router.push({ name: 'Chat', params: { 'username': username }})
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: `${this.$defaultUrl}/chat/rooms/`,  
      headers: this.setHeader()
    })
    .then(res => {
      console.log(res.data);
      this.rooms = res.data['rooms']
    })
  }
}
</script>

<style>
.bg {
  background-image: url('../assets/main_bg.jpg');
  background-size : 100%;
  background-repeat: repeat;
  position:absolute;
  width: 100%;
  height: 100%;
}
#inspire {
  background: none;
}
</style>