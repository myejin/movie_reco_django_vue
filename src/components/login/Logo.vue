<template>
  <div>
    <router-link :to="{name: 'Home'}">
      <img class="logo-size logo-position" src="@/assets/Logo.png" alt="">
    </router-link>
  </div>
</template>

<script>
export default {
  name:'Logo'
}
</script>

<style scoped>
.logo-size{
  width: 80px;
}

.logo-position {
  position: absolute;
  top:40px;
  left: 170px;
}
</style>