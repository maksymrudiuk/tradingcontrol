import { Auth } from '@/api/auth'
import { AUTH_REQUEST, AUTH_SUCCESS, AUTH_ERROR, AUTH_LOGOUT } from '../mutations/auth-mutation-types.js'
import { USER_REQUEST, SET_STAFF_TO_NULL } from '../mutations/user-mutation-types.js'
import { CLEAR_REPORT_AFTER_LOGOUT } from '../mutations/report-mutation-types.js'
import axios from 'axios'

const state = {
  token: localStorage.getItem('user-token') || '',
  status: 'logout',
  hasLoadedOnce: false
}

const getters = {
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status
}

const mutations = {
  [AUTH_REQUEST] (state) {
    state.status = 'loading'
  },
  [AUTH_SUCCESS] (state, token) {
    state.status = 'success'
    state.token = token
    state.hasLoadedOnce = true
  },
  [AUTH_ERROR] (state) {
    state.status = 'error'
    state.hasLoadedOnce = true
  },
  [AUTH_LOGOUT] (state) {
    state.status = 'logout'
    state.token = ''
  }
}

const actions = {
  [AUTH_REQUEST] ({ commit, dispatch }, data) {
    return new Promise((resolve, reject) => {
      commit(AUTH_REQUEST)
      Auth.authRequest(data)
        .then(response => {
          const token = response.data.token
          localStorage.setItem('user-token', token)
          // console.log('before' + token)
          axios.defaults.headers.common['Authorization'] = 'JWT ' + token
          // console.log('after' + token)
          commit(AUTH_SUCCESS, token)
          dispatch(USER_REQUEST)
          resolve(response)
        })
        .catch(err => {
          commit(AUTH_ERROR, err)
          localStorage.removeItem('user-token')
          reject(err)
        })
    })
  },
  [AUTH_LOGOUT] ({ commit }) {
    return new Promise((resolve, reject) => {
      commit(AUTH_LOGOUT)
      commit(CLEAR_REPORT_AFTER_LOGOUT)
      commit(SET_STAFF_TO_NULL)
      localStorage.removeItem('user-token')
      delete axios.defaults.headers.common['Authorization']
      resolve()
    })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
