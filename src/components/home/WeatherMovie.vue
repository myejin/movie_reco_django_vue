<template>
  <div class="carousel-position">
   <carousel
      :per-Page="2"
      :paginationEnabled="false"
      class="carousel-size">
        <slide     
          v-for="movie in weatherMovie"
          :key="movie.id"
          
          >
          <img class="img-size" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
         
        </slide>
    </carousel>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: 'WeatherMovie',
  components: {
    Carousel,
    Slide
  },
  computed:{
    ...mapState(['weatherMovie']),
  }
}
</script>

<style scoped>
.carousel-position {
  position: absolute;
  top:600px;
  left: 100px;
}
.carousel-size {
  width: 1000px;
  height:600px;
}
.img-size {
  width:100%;
  height: 100%;

}
</style>