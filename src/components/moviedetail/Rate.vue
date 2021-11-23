<template>
  <div>
    <v-container
    class="px-0"
    fluid
  >
    <v-radio-group v-model="radioGroup">
      <v-radio
        v-for="n in 5"
        :key="n"
        :label="`${n}`"
        :value="n"
      ></v-radio>
      <v-btn @click="selectRate">sub</v-btn>
    </v-radio-group>
  </v-container>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'Rate',
  data () {
      return {
        radioGroup: 1,
        rankCount:null,
        rankSum:null
      }
    },
  methods: {
    setHeader: function () {
      const token = localStorage.getItem('jwt')
      const header = {
        Authorization: `JWT ${token}`
      }
      return header 
    },
    selectRate:function () {
      axios({
        method:'post',
        url:`${this.$defaultUrl}/movies/${this.$route.params.movieId}/rate/`,
        data:{"rank": this.radioGroup},
        headers: this.setHeader(),
      })
      .then(res => {
        console.log(res)
        this.rankCount= res.rank_count
        this.rankSum= res.rank_sum
      })
      .catch(err=>{
        console.log(err)
      })
    }
  
  },
  
  
}
</script>

<style>

</style>