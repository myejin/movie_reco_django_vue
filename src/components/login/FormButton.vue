<template>
  <div class="form-position">
        
    <v-form class="form-size">
      <v-text-field
        label="Username"
        id="username"
        v-model="credentials.username"
      ></v-text-field>
    
      <v-text-field
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"

        :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.min,]"
        :type="show3 ? 'text' : 'password'"
        name="input-10-2"
        hint="At least 8 characters"
        value=""
        class="input-group--focused"
        @click:append="show3 = !show3"
      ></v-text-field>
    </v-form>

    <v-btn 
      class="form-size"
      @click="login"  
    >
      Login
    </v-btn>

    <div style="text-align:center; margin-top:15px">
      <router-link :to="{name: 'Signup'}" class="text-decoration-none">
        <v-btn text >Signup</v-btn>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'TextField',
  data () {
      return {
        show3: false,
        password: 'Password',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        },
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  methods: {
    login: function () {
      axios({
        method:'post',
        url :`${this.$defaultUrl}/accounts/api/token/`,
        data:this.credentials,
      })
      .then(res => {
        localStorage.setItem('jwt',res.data.access)
        localStorage.setItem('myName', this.credentials.username)
        this.$router.go()
        // this.getProfile()
      })
    },
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    getProfile: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/accounts/${this.myName}/profile/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.$store.dispatch("setProfile", res.data)
      })
    },
  },
  created: function () {
    if ('jwt' in localStorage) {
        this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
.form-position {
  position: absolute;
  top:250px;
  left: 60px;
}
.form-size {
  width: 300px;
}
</style>