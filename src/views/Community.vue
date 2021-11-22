<template>
  <div>
    <Article v-for="article of articles"
      :key="article.id"
      :article="article"
    >
    </Article>
  </div>
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
  },
  created: function () {
    this.getArticles()
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