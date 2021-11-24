<template>
  <v-app id="inspire">
    <div class="posting-container">
      <h2>영화 같이 볼까요?</h2>
      <p>{{ myName }}님과 가까운 분의 모집글부터 노출됩니다.</p>
      <div class="inner-container">
        <v-simple-table>
          <tr>
            <th>username</th>
            <th>movie</th>
            <th>go chat </th>
            <th v-if="show">created_at</th>
            <th v-if="show">address</th>
          </tr>
          <Article v-for="article of sortedArticles"
            :key="article.id"
            :article="article"
            @show-toggle="showToggle"
          >
          </Article>
        </v-simple-table>
    </div>
    </div>
  </v-app>
</template>
<script>
import Article from '@/components/article/Article.vue'
import axios from 'axios'

export default {
  name:'Community',
  components: {
    Article,
  },
  data: function () {
    return {
      articles: [],
      articleCount: 0,
      position: {
        latitude: 0,
        longitude: 0,
      },
      show: false,
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
    getArticles: function () {
      axios({
        method: 'get',
        url: `${this.$defaultUrl}/articles/`,  
        headers: this.setHeader()
      })
      .then(res => {
        this.articles = res.data['articles']
        this.articleCount = res.data['count']
      })
    },
    getPosition: function () {
      if('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(position => {
          this.position.latitude = position.coords.latitude
          this.position.longitude = position.coords.longitude
        }, err => {
          console.log(err)
        })
      } else {
        alert('위치정보를 사용할 수 없습니다.')
      }
    },
    getDistance: function (p1, p2) {
      const rad = x => (x * Math.PI) / 180 
      const R = 6371
      const lat1 = p1.latitude
      const lng1 = p1.longitude
      const lat2 = p2.latitude
      const lng2 = p2.longitude
      const dLat = rad(lat2-lat1)
      const dLon = rad(lng2-lng1)
      const a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(dLon/2) * Math.sin(dLon/2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
      return R * c 
    },
    showToggle: function () {
      this.show = !this.show
    }
  },
  computed: {
    sortedArticles: function () {
      const distArticles = this.articles.map(article => {
        const articlePos = {
          'latitude': article.latitude,
          'longitude': article.longitude
        }
        const ret = {
          ...article,
          'dist': this.getDistance(this.position, articlePos),
        }
        return ret
      })
      return distArticles.sort((a, b) => {
        return a.dist - b.dist 
      })
    },
    myName: function () {
      if ('myName' in localStorage) {
        return localStorage.getItem('myName')
      } else {
        return ''
      }
    }
  },
  created: function () {
    this.getArticles()
    this.getPosition()
  }
}

</script>

<style scoped>
.bg {
  background-image: url('../assets/main_bg.jpg');
  background-size : 100%;
  background-repeat: repeat;
  position:absolute;
  width: 100%;
  height: 100%;
}

#inspire {
  background: none;
}
</style>