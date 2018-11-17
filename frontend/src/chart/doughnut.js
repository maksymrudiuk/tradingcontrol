export const doughnutChartData = {
  type: 'pie',
  data: {
    labels: ['Наявно', 'Відсутньо'],
    datasets: [
      { // another line graph
        label: 'Товару у %',
        data: [70, 30],
        backgroundColor: [
          '#FF2F7E',
          '#FED451'
        ],
        borderColor: [
          '#FF2F7E',
          '#FED451'
        ],
        borderWidth: 2
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

export default doughnutChartData
