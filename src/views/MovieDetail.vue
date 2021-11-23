<template>
  <div>
    <span class="bg">
      <v-app id="inspire">
        <v-container >
          <v-row justify="space-between">
            
            <v-col sm="0" lg="2" >
              <v-img  src="@/assets/전통무늬1.png" alt=""></v-img>
            </v-col>

            <v-col class="pt-10 my-10 pb-16">
              <detail></detail>
            </v-col>

            <v-col sm="0" lg="2"  align-self="end">
              <v-img  src="@/assets/전통무늬2.png" alt=""></v-img>
            </v-col>
          
          </v-row>
        </v-container>
        <!-- <actors></actors> -->
      </v-app>
    </span>
  </div>
</template>

<script>
import Detail from '@/components/moviedetail/Detail'
// import Actors from '@/components/moviedetail/Actors'

export default {
  name:'MovieDetail',
  components: {
    Detail,
    // Actors,
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
  height: 2000px;
}

#inspire {
  background: none;
}

</style>