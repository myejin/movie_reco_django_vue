<template>
  <div class="bg">
    <div :v-if="seoulWeather">
      <img :src="weatherIcon" alt="">
      <p>{{seoulWeather.data.weather[0].main}}</p>
    </div>
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

export default {
  name:'Weather',

  computed: {
    ...mapState(['seoulWeather']),
    ...mapGetters(['isWeather','weatherIcon'])
  }
}
</script>

<style scoped>
.bg {
  background-image: url('../../assets/rain.jpg');
  background-size : 100%;
  margin: 0px 200px;
  height: 800px;
}
</style>