<template>
  <div>
    <router-link :to="{name: 'Chat'}">채팅하러가기</router-link>
    <!-- path에 들어갈 username 어떻게 설정하지? -->
    <!-- 아티클 컴포넌트도 만들자 -->
  </div>
</template>

<script>

export default {
  name:'Community',
  components: {
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