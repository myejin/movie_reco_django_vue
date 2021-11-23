import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    seoulWeather:[],
    weatherMovie: [],
    genreMovies:[]
  },
  mutations: {
    LOAD_WEATHER_DATA: function(state, res){
      state.seoulWeather = res
    },
    LOAD_WEATHER_MOVIE:function(state, res){
      state.weatherMovie = res
    },
    LOAD_GENRE_MOVIES:function(state,res) {
      state.genreMovies = res
    }
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
          genresN =  3
        } else if (response1.data.weather[0].main === "Clouds") {
          genresN =  15
        } 
        
        const response2 = await axios({
              method:'get',
              url:`http://127.0.0.1:8000/genres/${genresN}/movies/`,
            })
        console.log(response2, "???????")
        commit('LOAD_WEATHER_MOVIE', response2)
    },
    LoadGenreMovies: function ({commit}) {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/genres/1/movies/',
      })
      .then(res => {
        commit('LOAD_GENRE_MOVIES', res.data)
      })
    }
  },
  getters: {
    // isWeather: function (state) {
    //   return state.seoulWeather.data.weather ? true : false
    // },
    // isMovie: function (state) {
    //   return state.weatherMovie.data.Movies ? true : false
    // },
    weatherIcon: function (state) {
      const iconId = state.seoulWeather.data.weather[0].icon
      return `http://openweathermap.org/img/wn/${iconId}@2x.png`
    }
  }
})
