import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    seoulWeather:[],
    addWeatherData:[],
    weatherMovie: [],
    profile: {
      likeGenres: [],
      rateMovies: [],
      wishMovies: [],
    },
  },
  mutations: {
    LOAD_WEATHER_DATA: function(state, res){
      state.seoulWeather = res
    },
    LOAD_ADD_DATA: function(state,res) {
      state.addWeatherData = res
    },
    LOAD_WEATHER_MOVIE:function(state, res){
      state.weatherMovie = res
    },
    SET_PROFILE: function (state, res) {
      state.profile.likeGenres = res['like_genres']
      state.profile.rateMovies = res['rate_movies']
      state.profile.wishMovies = res['wish_movies']
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
        console.log(response1.data,"loadweatherdata")
        commit('LOAD_WEATHER_DATA',response1.data.weather[0])
        commit('LOAD_ADD_DATA',response1.data)

        let genresN = 1
        if (response1.data.weather[0].main === "Thunderstorm") {
            genresN = 5
        } else if (response1.data.weather[0].main === "Drizzle") {
            genresN =  9
        } else if (response1.data.weather[0].main === "Rain") {
          genresN =  11
        } else if (response1.data.weather[0].main === "Snow") {
          genresN =  14
        } else if (response1.data.weather[0].main === "Atmosphere") {
          genresN =  12
        } else if (response1.data.weather[0].main === "Clear") {
          genresN =  8
        } else if (response1.data.weather[0].main === "Clouds") {
          genresN =  15
        } 
        
        const response2 = await axios({
              method:'get',
              url:`http://127.0.0.1:8000/genres/${genresN}/movies/`,
            })
        console.log(response2, "???????")
        commit('LOAD_WEATHER_MOVIE', response2.data.movies)
    },
    setProfile: function (context, data) {
      context.commit('SET_PROFILE', data)
    },
  },
  getters: {
    nowTemp: function(state) {
      if (state.addWeatherData.main) {
        const nowT = Math.round(state.addWeatherData.main.temp - 273.15)
        return nowT
      } return ''
    },
    maxTemp: function(state) {
      if (state.addWeatherData.main) {
        const maxT = Math.round(state.addWeatherData.main.temp_max - 273.15)
        return maxT
      } return ''
    },
    minTemp: function(state) {
      if (state.addWeatherData.main) {
        const minT = Math.round(state.addWeatherData.main.temp_min - 273.15)
        return minT
      } return ''
    },

  }

})
