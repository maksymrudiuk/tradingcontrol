export const barChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  legend: {
    display: false,
    labels: {
      fontColor: 'black',
      fontSize: 12
    }
  },
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
      ticks: {
        padding: 15,
        maxRotation: 90
      },
      gridLines: {
        offsetGridLines: true
      }
    }]
  }
}

export default barChartOptions
