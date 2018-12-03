import { Report } from '@/api/report'
import { GET_REPORTS, GET_REPORT_SUCCESS, GET_REPORT_ERROR, CLEAR_REPORT_AFTER_LOGOUT } from '../mutations/report-mutation-types.js'
// import barChartData from '@/chart/bar.js'

const state = {
  reports: [],
  status: 'logout' // Report for one selected user
}

const getters = {
  reportStatus: state => state.status,
  getReports: state => state.reports,
  getBarDatacollection: state => {
    const datacollection = {
      datasets: [
        {
          data: null,
          label: 'Наявність товару',
          borderWidth: 3
        }
      ]
    }
    const labels = []
    const data = []

    for (let item in state.reports) {
      labels.push(state.reports[item].store.name)
      data.push(state.reports[item].assortment_percent)
    }

    datacollection.labels = labels
    datacollection.datasets[0]['data'] = data

    return datacollection
  },
  getPieDatacollection: state => {
    const datacollection = {
      labels: ['Наявно', 'Відсутньо'],
      datasets: [{
        data: null,
        label: 'Наявність товару',
        borderWidth: 0,
        backgroundColor: [
          'rgba(123, 191, 8, .75)',
          'rgba(191, 17, 5, .75)'
        ]
      }]
    }
    const data = []
    var sum = null
    for (let item in state.reports) {
      sum += state.reports[item].assortment_percent
    }
    var positive = Math.round(sum / state.reports.length)
    data.push(positive)
    data.push(100 - positive)
    datacollection.datasets[0]['data'] = data
    return datacollection
  }
}

const mutations = {
  [GET_REPORTS] (state) {
    state.status = 'loading'
  },
  [GET_REPORT_SUCCESS] (state, response) {
    state.status = 'success'
    state.reports = response
  },
  [GET_REPORT_ERROR] (state) {
    state.status = 'error'
  },
  [CLEAR_REPORT_AFTER_LOGOUT] (state) {
    state.status = 'logout'
    state.reports = []
  }
}

const actions = {
  [GET_REPORTS] ({ commit }) {
    return new Promise((resolve, reject) => {
      commit(GET_REPORTS)
      Report.getReports()
        .then(response => {
          commit(GET_REPORT_SUCCESS, response)
          resolve(response)
        })
        .catch(err => {
          commit(GET_REPORT_ERROR, err)
          reject(err)
        })
    })
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
