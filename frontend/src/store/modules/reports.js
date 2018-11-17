const state = {
  report: {
    name: '1347548',
    routes: [
      {
        id: '1',
        name: 'Ашан',
        t_start: '9.00',
        t_finish: '9.30',
        t_delta: '30',
        goods_status: '0'
      },
      {
        id: '3',
        name: 'АТБ',
        t_start: '9.50',
        t_finish: '10.20',
        t_delta: '30',
        goods_status: '60'
      },
      {
        id: '4',
        name: 'Billa',
        t_start: '10.40',
        t_finish: '11.40',
        t_delta: '60',
        goods_status: '95'
      }
    ]
  } // Report for one selected user
}

const getters = {
  report: state => state.report
}

const actions = {

}

const mutations = {

}

export default {
  state,
  getters,
  actions,
  mutations
}
