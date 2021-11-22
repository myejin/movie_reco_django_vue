import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    seoulWeather:'',
    weatherMovie: []
  },
  mutations: {
    LOAD_WEATHER_DATA: function(state, res){
      state.seoulWeather = res
    },
    LOAD_WEATHER_MOVIE: function(state, res) {
      state.weatherMovie = res
    }
  },
  actions: {
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
        commit('LOAD_WEATHER_DATA',res )
      }))
    },
    LoadWeatherMovie: function ({commit}) {
      const genre_pk = 19
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/genres/${genre_pk}/movies/`,
      })
      .then((res => {
        console.log(res);
        commit('LOAD_WEATHER_MOVIE', res)
      }))
      .catch((err => {
        console.log(err);
      }))
    }
  },
})
