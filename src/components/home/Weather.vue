<template>
  <div>
    {{seoulWeather}}
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name:'Weather',
  created: function () {
    this.$store.dispatch('LoadWeatherData')
  },
  computed: {
    ...mapState(['seoulWeather'])
  }
}
</script>

<style>

</style>