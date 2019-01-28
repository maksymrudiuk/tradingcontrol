// Vue imports
import Vue from 'vue'
import Router from 'vue-router'
// Component imports
import Greeting from '@/components/Greeting.vue'
import SignIn from '@/components/sign-in/Sign-in.vue'
import Home from '@/components/content/main/Home.vue'
import Content from '@/components/content/Content.vue'
import Goods from '@/components/content/main/Goods.vue'
import Staff from '@/components/content/main/Staff.vue'
import Reports from '@/components/content/main/Reports.vue'
import Settings from '@/components/content/main/Settings.vue'
import RAlbum from '@/components/content/main/gallery/RAlbum'
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
  next('/sign-in')
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
      name: 'main',
      component: Greeting
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Content,
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
          component: RAlbum,
          props: true
        }
      ]
    },
    {
      path: '/sign-in',
      name: 'sign-in',
      component: SignIn,
      beforeEnter: ifNotAuthenticated
    }
  ]
})
