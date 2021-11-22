<template>
  <div :v-if="isMovie">
    <div 
 
    >
      <p>{{weatherMovie.data.movies}}</p>

    </div>
   
  </div>
</template>

<script>
import { mapState,mapGetters } from 'vuex'

export default {
  name: 'WeatherMovie',
  computed:{
    ...mapState(['weatherMovie']),
    ...mapGetters(['isMovie'])
  }
}
</script>

<style>

</style>