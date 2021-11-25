<template>
  <div>
    <span class="bg"></span>
      <v-app id="inspire">
        <v-container class="mt-10" >
          <v-row>
<!--             
            <v-col sm="0" lg="2" >
              <v-img  src="@/assets/전통무늬1.png" alt=""></v-img>
            </v-col> -->

            <v-col>
              <detail></detail>
            </v-col>

            <!-- <v-col sm="0" lg="2" >
              <v-img  src="@/assets/전통무늬2.png" alt=""></v-img>
            </v-col> -->
          
          </v-row>
        </v-container>
      </v-app>

  </div>
</template>

<script>
import Detail from '@/components/moviedetail/Detail'

export default {
  name:'MovieDetail',
  components: {
    Detail,
  },
  created: function () {
    if (!('jwt' in localStorage)) {
      this.$router.push({ name: 'Home'})
    }
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