import { HTTP } from './common'

export const Report = {
  getReports (days) {
    return HTTP.get('/reports/list', {
      params: {
        fordays: days
      }
    }).then(response => {
      return response.data
    })
  }
}
