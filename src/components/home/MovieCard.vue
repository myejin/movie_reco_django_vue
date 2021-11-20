<template>
  <div>
    <h1>{{ movieCard.title }}</h1>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  }
}
</script>

<style>

</style>