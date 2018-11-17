export const barChartData = {
  type: 'bar',
  data: {
    labels: ['Ашан', 'АТБ', 'Billa'],
    datasets: [
      { // another line graph
        label: 'Наявність товару у %',
        data: [95, 65, 35],
        backgroundColor: [
          'rgba( 71, 183, 132, .5)', // Green
          'rgba(255, 206, 75,  .5)', // Green
          'rgba(245, 36,  94,  .5)' // Green
        ],
        borderColor: [
          '#47b784',
          '#FFCE4B',
          '#F5245E'
        ],
        borderWidth: 3
      }
    ]
  },
  options: {
    responsive: true,
    lineTension: 1,
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          padding: 25
        }
      }]
    }
  }
}

export default barChartData
