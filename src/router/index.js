import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import MovieDetail from '../views/MovieDetail.vue'
import GenreMovies from '../views/GenreMovies.vue'
import Chat from '../views/Chat.vue'
import Community from '../views/Community.vue'
import Profile from '../views/Profile.vue'
import ChatRooms from '../views/ChatRooms.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path:'/profile/:username',
    name:'Profile',
    component: Profile
  },
  {
    path:'/movie/:movieId',
    name:'MovieDetail',
    component: MovieDetail
  },
  {
    path:'/genres/:genreId/movies',
    name:'GenreMovies',
    component: GenreMovies
  },

  {
    path:'/community',
    name:'Community',
    component: Community
  },
  {
    path:'/chat/:username',
    name:'Chat',
    component: Chat
  },
  {
    path:'/chatrooms',
    name:'ChatRooms',
    component: ChatRooms
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior () {
    return { x: 0, y: 0 }
  }
})

export default router
