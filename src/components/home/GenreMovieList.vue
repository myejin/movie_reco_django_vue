<template>
  <div>
    <div v-for="genre of profile.likeGenres"
      :key="genre.id"
    >
      <genre-movie-item
        :genreId="genre.id"
      ></genre-movie-item>
    </div>

  </div>
</template>

<script>
import GenreMovieItem from './GenreMovieItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'GenreMovieList',
  components: {
    GenreMovieItem,
  },
  computed: {
    ...mapState([
      'profile',
    ]),
  }
}
</script>

<style>

</style>