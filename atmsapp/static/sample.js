// Data for the bar chart
var data = {
  labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'],
  datasets: [{
    label: 'Dataset 1',
    data: [20, 12, 30, 15, 40, 25, 50],
    backgroundColor: 'rgba(75, 192, 192, 0.2)', // Color of the bars
    borderColor: 'rgba(75, 192, 192, 1)', // Color of the bar borders
    borderWidth: 1 // Width of the bar borders
  }]
};

// Chart configuration
var config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    scales: {
      x: {
        beginAtZero: true
      },
      y: {
        beginAtZero: true
      }
    }
  }
};

// Create the bar chart
var myChart = new Chart(document.getElementById('barChart'), config);