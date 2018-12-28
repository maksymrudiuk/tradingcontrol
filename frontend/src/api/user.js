import { HTTP } from './common'

export const User = {
  userRequest () {
    return HTTP.get('/accounts/users').then(response => {
      return response.data
    })
  },
  getMyStaff () {
    return HTTP.get('/accounts/staff').then(response => {
      return response.data
    })
  }
}
