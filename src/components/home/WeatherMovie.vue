<template>
  <div>
    {{weatherMovie.data}}
    {{seoulWeather}}
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MovieCard',
  created: function () {
    this.$store.dispatch('LoadWeatherMovie')
  },
  computed: {
    ...mapState([
      'weatherMovie',
      ])
  }
}
</script>

<style>

</style>