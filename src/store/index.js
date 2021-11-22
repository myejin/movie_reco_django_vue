import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    seoulWeather:[],
    weatherMovie: []
  },
  mutations: {
    LOAD_WEATHER_DATA: function(state, res){
      state.seoulWeather = res
    },
    LOAD_WEATHER_MOVIE:function(state, res){
      state.weatherMovie = res
    },
  },
  actions: {
    async LoadWeatherMovie ({commit}) {
      const response1 = await axios({
        method:'get',
        url: 'https://api.openweathermap.org/data/2.5/weather',
        params: {
          lat:37.56826,
          lon: 126.977829,
          APPID: process.env.VUE_APP_WEATHER_APPID
        }
      })
        console.log()
        console.log(response1,"loadweatherdata")
        commit('LOAD_WEATHER_DATA',response1)

        let genresN = 1
        if (response1.data.weather[0].description === "broken clouds") {
            genresN = 19
        } else {
            genresN = 9
        }
        
        const response2 = await axios({
              method:'get',
              url:`http://127.0.0.1:8000/genres/${genresN}/movies/`,
            })
        console.log(response2, "???????")
        commit('LOAD_WEATHER_MOVIE', response2)
    },
  },
  getters: {
    isWeather: function (state) {
      return state.seoulWeather.data.weather ? true : false
    },
    isMovie: function (state) {
      return state.weatherMovie.data.Movies ? true : false
    },
    weatherIcon: function (state) {
      const iconId = state.seoulWeather.data.weather[0].icon
      return `http://openweathermap.org/img/wn/${iconId}@2x.png`
    }
  }
})
