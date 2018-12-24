export const barChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true,
        padding: 25,
        max: 120
      }
    }],
    xAxes: [{
      maxBarThickness: 100,
      categoryPercentage: 0.95,
      barPercentage: 0.95,
      // barThickness: 'flex',
      ticks: {
        padding: 15
      },
      gridLines: {
        offsetGridLines: true
      }
    }]
  }
}

export default barChartOptions
