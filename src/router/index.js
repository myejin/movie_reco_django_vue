import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Chat from '../views/Chat.vue'
import Community from '../views/Community.vue'


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
    path:'/movie/:movieId',
    name:'MovieDetail',
    component: MovieDetail
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
