<template>
  <div>
    <v-card
      class="mx-auto"
      max-width="344"
      @click="goDetail"
    >
      <v-img
        :src="`https://image.tmdb.org/t/p/original${posterPath}`"
        height="200px"
      ></v-img>

      <v-card-title class="cardTitle">
        {{title}}
      </v-card-title>

      <v-card-actions>
        <v-btn
          color="orange lighten-2"
          text
        >
          DETAIL
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
export default {
  name:'MovieCard',
  data: () => ({
      show: false,
    }),
  props: {
    id: Number,
    title: String,
    posterPath: String,
  },
  methods: {
    goDetail: function () {
        this.$router.push({name: 'MovieDetail', params: { movieId: this.id }})
    }
  }
}
</script>

<style>
.cardTitle {
  padding: 1rem;
  font-size: 25px;
  white-space: nowrap; 
  word-break: normal; 
  overflow: hidden; 
  text-overflow: ellipsis;
}
</style>