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
    LoadMovieCards: function () {
      const token = localStorage.getItem('JWT')
      // const header = {
      //   Authorization: `JWT ${token}`
      // }
      axios({
        method: 'post',
        url: 'http://3.34.140.15/movies/init/',
        Authorization: `JWT ${token}`
      })
        .then((res) => {
          console.log(res)
          // commit('LOAD_MOVIE_CARDS')
        })
        .catch((err) =>{
          console.log(err)
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
