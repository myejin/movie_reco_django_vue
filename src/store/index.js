import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards:[],
    seoulWeather:''
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, res) {
      state.movieCards = res
    },
    LOAD_WEATHER_DATA: function(state, res){
      state.seoulWeather = res
    }
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: process.env.VUE_APP_TMDB_API_KEY,
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    },
    LoadWeatherData: function ({commit}) {
      axios({
        method:'get',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
          lat:37.56826,
          lon: 126.977829,
          APPID: process.env.VUE_APP_WEATHER_APPID
        }
      })
      .then((res => {
        console.log(res)
        commit('LOAD_WEATHER_DATA',res.data.weather[0].main )
      }))
    }
    
  },
})
