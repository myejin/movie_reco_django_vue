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
        :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.min]"
        :type="show3 ? 'text' : 'password'"
        name="input-10-2"
        hint="At least 8 characters"
        value=""
        class="input-group--focused"
        @click:append="show3 = !show3"
      ></v-text-field>

      <v-text-field
        id="password2"
        v-model="credentials.password2"
        @keyup.enter="signup"
        :append-icon="show3 ? 'mdi-eye' : 'mdi-eye-off'"
        :rules="[rules.required, rules.min]"
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
      @click="signup"  
    >
      Signup
    </v-btn>

    <div style="text-align:center; margin-top:15px">
      <router-link :to="{name: 'Login'}" class="text-decoration-none">
        <v-btn text >Login</v-btn>
      </router-link>
    </div>
  </div>
</template>

<script >
import axios from 'axios'

export default {
  name:'TextField',
  data: function () {
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
          password2: ''
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: `${this.$defaultUrl}/accounts/signup/`,
        data: this.credentials
      })
        .then(() => {
          this.$router.push({name:'Login'})
        })
        .catch(err => {
          console.log(err)
          if (err.response['status'] === 400) {
            alert('이미 사용 중인 이름입니다.')
          }
        })
    }
  }
}
</script>

<style scoped>
.form-position {
  position: absolute;
  top:210px;
  left: 60px;
}
.form-size {
  width: 300px;
}
</style>