import { User } from '@/api/user'
import { USER_REQUEST, USER_ERROR, USER_SUCCESS, GET_STAFF, SET_STAFF_TO_NULL } from '../mutations/user-mutation-types.js'
import { AUTH_LOGOUT } from '../mutations/auth-mutation-types.js'

const state = {
  profile: {},
  status: 'logout',
  staff: []
}

const getters = {
  getStaff: state => state.staff,
  getProfile: state => state.profile,
  isProfileLoaded: state => !!state.profile.username,
  isDirector: state => state.profile.role === 'Директор'
}

const mutations = {
  [USER_REQUEST] (state) {
    state.status = 'loading'
  },
  [USER_SUCCESS] (state, response) {
    state.status = 'success'
    state.profile = response
  },
  [USER_ERROR] (state) {
    state.status = 'error'
  },
  [AUTH_LOGOUT] (state) {
    state.profile = {}
    state.status = 'logout'
  },
  [GET_STAFF] (state, response) {
    state.staff = response
  },
  [SET_STAFF_TO_NULL] (state) {
    state.staff = []
  }
}

const actions = {
  [USER_REQUEST] ({ commit, dispatch }) {
    commit(USER_REQUEST)
    User.userRequest()
      .then(response => {
        commit(USER_SUCCESS, response)
      })
      .catch(resp => {
        commit(USER_ERROR)
        dispatch(AUTH_LOGOUT)
      })
  },
  [GET_STAFF] ({ commit }) {
    User.getMyStaff()
      .then(response => {
        commit(GET_STAFF, response)
      })
      .catch(resp => {
        commit(SET_STAFF_TO_NULL)
      })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
