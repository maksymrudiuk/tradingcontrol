import { HTTP } from './common'

export const Auth = {
  authRequest (config) {
    return HTTP.post('token-auth/', config)
      .then(response => {
        return response
      })
  }
}
