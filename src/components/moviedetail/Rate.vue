<template>
  <div>
    <div style="display:flex; justify-content:center; margin:0px 400px">
      <h4 class="my-4">내 평점:</h4>
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
    <h2>총 평점 : {{ rank }}</h2>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'Rate',
  props: {
    rank: Number,
  },
  data () {
      return {
        items: [1, 2, 3, 4, 5],
        rankNum: 0,
        rankCount: 0,
        rankSum: 0,
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
        console.log(res.data);
        this.rankCount = res.data.rank_count
        this.rankSum = res.data.rank_sum
        this.rank = Math.round(this.rankSum / this.rankCount * 10) / 10
        alert('평점이 추가 또는 수정되었어요.')
      })
    },
    deleteRate:function () {
      axios({
        method:'delete',
        url:`${this.$defaultUrl}/movies/${this.$route.params.movieId}/rate/`,
        headers: this.setHeader(),
      })
      .then((res) => {
        this.rankCount = res.data.rank_count
        this.rankSum = res.data.rank_sum
        this.rank = Math.round(this.rankSum / this.rankCount * 10) / 10
        alert('이전에 등록한 평점을 삭제합니다.')
      })
      .catch(err =>{
        if (err.response['status'] === 404) {
          alert('등록된 평점이 없어요.')
        }
      })
    }
  },
}
</script>

<style>

</style>