import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.prototype.$defaultUrl = 'http://127.0.0.1:8000';
Vue.prototype.$webSockettUrl = 'ws://127.0.0.1:8000/ws/chat';
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')