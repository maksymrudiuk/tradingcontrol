import { Report } from '@/api/report'
import { GET_REPORTS, GET_REPORT_SUCCESS, GET_REPORT_ERROR,
  CLEAR_REPORT_AFTER_LOGOUT, GET_RETRIEVE_REPORT, GET_STORE_PHOTOS } from '../mutations/report-mutation-types.js'

const state = {
  reports: [],
  status: '',
  retrieve: {
    store: Object,
    owner: Object
  },
  // retrieve: {},
  storePhotos: []
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
  },
  getStoreMarkers: state => {
    const markers = []
    for (let item in state.reports) {
      const position = {}
      const title = state.reports[item].store.name
      position['lat'] = state.reports[item].store.lat
      position['lng'] = state.reports[item].store.lon
      markers.push({ position, title })
    }
    return markers
  },
  retrieveReport: state => {
    return state.retrieve
  },
  storePhotos: state => {
    return state.storePhotos
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
    state.retrieve = {}
    state.storePhotos = []
  },
  [GET_RETRIEVE_REPORT] (state, response) {
    state.status = 'get detail report'
    state.retrieve = response
  },
  [GET_STORE_PHOTOS] (state, response) {
    state.storePhotos = response
  }
}

const actions = {
  [GET_REPORTS] ({ commit }, days) {
    return new Promise((resolve, reject) => {
      commit(GET_REPORTS)
      Report.getReports(days)
        .then(response => {
          commit(GET_REPORT_SUCCESS, response)
          resolve(response)
        })
        .catch(err => {
          commit(GET_REPORT_ERROR, err)
          reject(err)
        })
    })
  },
  [GET_RETRIEVE_REPORT] ({ commit }, id) {
    return new Promise((resolve, reject) => {
      commit(GET_REPORTS)
      Report.retrieveReport(id)
        .then(response => {
          commit(GET_RETRIEVE_REPORT, response)
          resolve(response)
        })
        .catch(err => {
          commit(GET_REPORT_ERROR, err)
          reject(err)
        })
    })
  },
  [GET_STORE_PHOTOS] ({ commit }, id) {
    return new Promise((resolve, reject) => {
      Report.getStorePhotos(id)
        .then(response => {
          commit(GET_STORE_PHOTOS, response)
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
