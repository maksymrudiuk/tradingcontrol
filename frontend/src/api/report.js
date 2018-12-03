import { HTTP } from './common'

export const Report = {
  getReports () {
    // console.log(config)
    return HTTP.get('/reports/list').then(response => {
      return response.data
    })
  }
}
