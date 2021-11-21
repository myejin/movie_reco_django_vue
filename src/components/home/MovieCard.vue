<template>
  <div>
    <carousel>
      <slide>
        <h1>{{ movieCard.title }}</h1>
      </slide>
    </carousel>
    
  </div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
export default {
  name: 'MovieCard',
   components: {
    Carousel,
    Slide
  },
  props: {
    movieCard: Object
  }
}
</script>

<style>

</style>