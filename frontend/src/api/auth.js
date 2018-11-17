import { HTTP } from './common'

export const Auth = {
  authRequest (config) {
    // console.log(config)
    return HTTP.post('/token-auth/', config)
      .then(response => {
        return response
      })
  }
}
