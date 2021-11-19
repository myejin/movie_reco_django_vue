<template>
  <div class="form-position">
        
    <v-form class="form-size">
      <v-text-field
        label="Username"
      ></v-text-field>
    
      <v-text-field
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

    <v-btn class="form-size">
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
export default {
  name:'TextField',
  data () {
      return {
        show3: false,
        password: 'Password',
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          emailMatch: () => (`The email and password you entered don't match`),
        },
      }
    },
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