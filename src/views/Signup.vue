<template>
  <div>
    <span class="bg"></span>
      <v-app id="inspire">
        <v-container style="max-width:1800px" class="mx-0">
          <v-row justify="space-between">
            
            <v-col sm="0" lg="2" >
              <v-img  src="@/assets/flower2.png" alt=""></v-img>
            </v-col>

            <v-col cols="auto" class="pt-0">
              <card></card>
            </v-col>

            <v-col sm="0" lg="2"  align-self="end">
              <v-img  src="@/assets/flower1.png" alt=""></v-img>
            </v-col>
          
          </v-row>
        </v-container>
      </v-app>
  </div>
</template>

<script>
import Card from '../components/signup/Card.vue'


export default {
  name:'Signup',
  components: {
    Card,
  }
}

</script>

<style scoped>
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