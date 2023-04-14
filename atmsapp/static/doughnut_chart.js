//doughnut
var ctxD = document.getElementById("doughnutChart").getContext('2d');
var myLineChart = new Chart(ctxD, {
  type: 'doughnut',
  data: {
    labels: ["Extreme Traffic", "Normal", "Light Traffic", "Traffic", "Mulfunctioned"],
    datasets: [{
      data: [15, 15, 5, 5, 5],
      backgroundColor: ["red", "green", "yellow", "orange", "gray"],
      hoverBackgroundColor: ["#FF5A5E", "#5AD3D1", "#FFC870", "#A8B3C5", "#616774"]
    }]
  },
  options: {
    responsive: true
  }
});


