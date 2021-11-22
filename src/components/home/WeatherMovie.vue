<template>
  <div class="carousel-position">
   <carousel
   style="width:600px; height:60%;"
   per-Page="4">
    <slide     
      v-for="movie in weatherMovie.data.movies"
      :key="movie.id"
      
      >
      <img class="img-size" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" alt="">
      <span>{{movie.title}}</span>
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
  top:40px;
  left: 170px;
}
.img-size {
  width:50%;
  height: 2rem;
}
</style>