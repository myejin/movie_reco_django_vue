<template>
  <div >
    <links></links>
    <div class="center-position">
      <img height="400px" src="@/assets/영화포스터샘플.jpg" alt="">
      
      <div class="ms-16">
        <h1>영화제목</h1>
        <img width="80%" src="@/assets/detail_title.png" alt="">

      </div>
    </div>
  
  </div>
</template>

<script>
import Links from '@/components/moviedetail/Links'

export default {
  name:'Detail',
  components: {
    Links
  }
}
</script>

<style scoped>
.center-position {
  display:flex; 
  justify-content:center;
}

</style>