// Vue imports
import Vue from 'vue'
import Router from 'vue-router'
// Component imports
import Greeting from '@/components/NestedComponents/Greeting.vue'
import VLogin from '@/components/CommonComponents/VLogin.vue'
import Home from '@/components/NestedComponents/Home.vue'
import VContainer from '@/components/CommonComponents/VContainer.vue'
import Goods from '@/components/NestedComponents/Goods.vue'
import Staff from '@/components/NestedComponents/Staff.vue'
import Reports from '@/components/NestedComponents/Reports.vue'
import Settings from '@/components/NestedComponents/Settings.vue'
import DetailAssortmentReport from '@/components/NestedComponents/DetailAssortmentReport'
// Store imports
import store from '@/store.js'

Vue.use(Router)

const ifNotAuthenticated = (to, from, next) => {
  if (!store.getters.isAuthenticated) {
    next()
    return
  }
  next('/')
}

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next()
    return
  }
  next('/accounts/signin')
}

const ifDirector = (to, from, next) => {
  if (store.getters.isDirector) {
    next()
    return
  }
  next('/dashboard/home')
}

export default new Router({
  // mode: 'history', if mode active don`t have absolute reload
  routes: [
    {
      path: '/',
      name: 'greeting',
      component: Greeting
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: VContainer,
      beforeEnter: ifAuthenticated,
      children: [
        {
          path: 'home',
          component: Home
        },
        {
          path: 'goods',
          component: Goods,
          beforeEnter: ifDirector
        },
        {
          path: 'staff',
          component: Staff,
          beforeEnter: ifDirector
        },
        {
          path: 'settings',
          component: Settings
        },
        {
          path: 'reports',
          component: Reports
        },
        {
          path: 'reports/:reportId/',
          name: 'reportDetails',
          component: DetailAssortmentReport,
          props: true
        }
      ]
    },
    {
      path: '/accounts/signin',
      name: 'login',
      component: VLogin,
      beforeEnter: ifNotAuthenticated
    }
  ]
})
