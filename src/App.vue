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

      <v-toolbar-title>Title</v-toolbar-title>
    </v-app-bar>
    <router-view/>
    <v-navigation-drawer
      v-model="drawer"
      absolute
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
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>
              <router-link @click.native="logout" to="#">
                Logout
              </router-link>
            </v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</div>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
      drawer: false,
      group: null,
  }),
  methods:{
    logout: function () {
      localStorage.removeItem('jwt')
      this.$router.push({name:'Login'})
    }
  },

};

</script>
