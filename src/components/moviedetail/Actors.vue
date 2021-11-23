<template>
  <div class="mt-16">
    <div class="bg">
      <v-slide-group
        class="pa-4 mx-auto"
        style="width:75%;"
      >
        <v-slide-item
          v-for="n in 15"
          :key="n"
        >
          <v-card
            class="ma-4"
            height="250"
            width="150"
          >
            <img width="100%" height="200" src="../../assets/actor_ex.jpg" alt="">
            <p>name</p>
          </v-card>
        </v-slide-item>
      </v-slide-group>

    </div>
    
  </div>
</template>

<script>
export default {
  name:'Actors',
}
</script>

<style scoped>
.bg {
  background-image: url('../../assets/actor_bg.png');
  background-size : 100%;
  position:absolute;
  width: 100%;
  height: 3000px;
}


</style>