<template>
  <div class="bg">
   <router-link :to="{name: 'Login'}">
     <img class="img-size" src="@/assets/Logo.png" alt="">
    </router-link>

    <div>
      <input type="text">
    </div>

    <div>
      <input type="text">
    </div>

    <div>
      <input type="text">
    </div>

    <button>Signup</button>
    <!-- <img style="width:100px" src="../../assets/노리개.png" alt=""> -->
    <div style="padding-bottom: 500px"></div>
  </div>
</template>

<script>
export default {
  name:'Signup'
}
</script>

<style scoped>
.bg {
  background-image: url('../../assets/accounts_bg.jpg');
  background-repeat: no-repeat;
  background-size : 100% ; 
}

.img-size {
  width:80px;
  margin:80px;
}



</style>