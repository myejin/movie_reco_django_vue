<template>
  <div>
    <!-- <span class="bg"></span> -->
    <room></room>
  </div>
</template>

<script>
import Room from '@/components/chat/Room.vue'


export default {
  name:'Chat',
  components: {
    Room,
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