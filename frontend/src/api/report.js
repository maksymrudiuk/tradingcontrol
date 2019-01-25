import { HTTP } from './common'

export const Report = {
  getReports (days) {
    return HTTP.get('reports/', {
      params: {
        fordays: days
      }
    }).then(response => {
      return response.data
    })
  },
  retrieveReport (id) {
    return HTTP.get('reports/' + id + '/detail/'
    ).then(response => {
      return response.data
    })
  }
}
