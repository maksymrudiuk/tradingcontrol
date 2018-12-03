import { User } from '@/api/user'
import { USER_REQUEST, USER_ERROR, USER_SUCCESS } from '../mutations/user-mutation-types.js'
import { AUTH_LOGOUT } from '../mutations/auth-mutation-types.js'

const state = {
  profile: {},
  status: 'logout'
}

const getters = {
  getProfile: state => state.profile,
  isProfileLoaded: state => !!state.profile.username
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
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
