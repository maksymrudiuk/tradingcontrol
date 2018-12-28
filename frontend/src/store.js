import Vue from 'vue'
import Vuex from 'vuex'
import user from './store/modules/user.js'
import auth from './store/modules/auth.js'
import report from './store/modules/reports.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    user,
    auth,
    report
  }
})
