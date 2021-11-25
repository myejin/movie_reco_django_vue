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
          <v-hover>
            <template v-slot:default="{ hover }">
              <v-card
                class="mx-auto"
                max-width="344"
              >
                <v-img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"></v-img>

                <v-card-text style="height:7rem">
                  <h2 class="text-h6 ">
                    {{movie.title}}
                  </h2>
                </v-card-text>

            

                <v-fade-transition>
                  <v-overlay
                    v-if="hover"
                    absolute
                    color="#036358"
                  >
                    <router-link class=" text-decoration-none"  :to="{name: 'MovieDetail', params: { movieId:movie.id }}">
                    <v-btn>See more info</v-btn>
                    </router-link>
                  </v-overlay>
                </v-fade-transition>
              </v-card>
            </template>
          </v-hover>
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
  data: () => ({
      overlay: false,
    }),
  computed:{
    ...mapState(['weatherMovie']),
  },
}
</script>

<style scoped>
.carousel-position {
  position: absolute;
  top:500px;
  left: 90px;
}
.carousel-size {
  width: 1000px;
  height:600px;
}
.img-size {
  width:100%;
  height: 100%;
  padding: 2rem;
}
</style>