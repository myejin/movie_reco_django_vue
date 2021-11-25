<template>
<div>

  <v-card
    class="mx-auto overflow-hidden"
  >

    <v-app-bar
      src="./assets/main_bg.jpg"
      fixed
      style="position:sticky"
    >
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-toolbar-title><router-link style="text-decoration:none; color:black;" :to="{name: 'Home'}">Home</router-link></v-toolbar-title>
      <v-spacer></v-spacer>
      <search-movie></search-movie>
      
    </v-app-bar>

    <router-view/>
    <v-navigation-drawer
      v-model="drawer"
      fixed
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link style="text-decoration:none; color:black;" :to="{name: 'Home'}">Home</router-link>
            </v-list-item-title>
          </v-list-item>
          
          <div v-if="!isLogin">
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" :to="{name: 'Signup'}">Signup</router-link>
              </v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link  style="text-decoration:none; color:black;" :to="{name: 'Login'}">Login</router-link>
              </v-list-item-title>
            </v-list-item>
          </div>

          <div v-else>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account-edit</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" :to="{name: 'Profile', params: { username: myName }}">Profile</router-link>
              </v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-chat</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" :to="{name: 'ChatRooms' }">Chat</router-link>
              </v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-filmstrip</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" :to="{name: 'GenreMovies', params:{genreId:1}}">Movie List</router-link>
              </v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account-multiple</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" :to="{name: 'Community'}">Community</router-link>
              </v-list-item-title>
            </v-list-item>

            <v-list-item>
              <v-list-item-icon>
                <v-icon block>mdi-logout</v-icon>
              </v-list-item-icon>
              <v-list-item-title>
                <router-link style="text-decoration:none; color:black;" @click.native="logout" to="#">
                  Logout
                </router-link>
              </v-list-item-title>
            </v-list-item>
          </div>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</div>
</template>

<script>
import SearchMovie from '@/components/home/SearchMovie.vue'

export default {
  name: 'App',
  components:{
    SearchMovie
  },
  data: () => ({
      drawer: false,
      group: null,
  }),
  methods:{
    logout: function () {
      localStorage.removeItem('jwt')
      localStorage.removeItem('myName')
      this.$router.go()
    }
  },
  computed: {
    isLogin: function () {
      if ('jwt' in localStorage) {
        return true 
      } else {
        return false 
      }
    },
    myName: function () {
      return localStorage.getItem('myName')
    }
  }
};

</script>
