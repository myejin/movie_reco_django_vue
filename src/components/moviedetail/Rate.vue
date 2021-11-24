<template>
  <div style="display:flex; justify-content:center; margin:0px 400px">
    <v-select
      style="width:20%"
      :items="items"
      v-model="rankNum"
      label="rate"
      solo
    ></v-select>
      <v-btn large class="ms-5 " @click="selectRate">sub</v-btn>
      <v-btn large class="ms-3 " @click="deleteRate">del</v-btn>

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'Rate',
  data () {
      return {
        items: [1, 2, 3, 4, 5],
        rankNum:0,
        rankCount:'',
        rankSum:''
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
        data:{"rank": this.rankNum},
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
    },
    deleteRate:function () {
      axios({
        method:'delete',
        url:`${this.$defaultUrl}/movies/${this.$route.params.movieId}/rate/`,
        headers: this.setHeader(),
      })
      .then(res => {
        console.log(res)
      })
      .catch(err =>{
        console.log(err)
      })
    }
  
  },
  
  
}
</script>

<style>

</style>