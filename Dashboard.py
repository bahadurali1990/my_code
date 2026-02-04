<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Isometric Dashboard Demo</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    body {
      background: #f0f2f5;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .iso-dashboard {
      position: relative;
      transform: skewY(-10deg) rotateX(20deg);
      perspective: 1000px;
    }

    .iso-screen {
      width: 500px;
      height: 300px;
      background: #fff;
      border-radius: 12px;
      box-shadow: 0 15px 30px rgba(0,0,0,0.2);
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-gap: 20px;
      padding: 20px;
    }

    .chart-box {
      background: #e3e9f0;
      border-radius: 8px;
      padding: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    canvas {
      max-width: 100%;
      max-height: 100%;
    }

    .iso-labels {
      margin-top: 20px;
      text-align: center;
      font-weight: bold;
      color: #333;
    }

    .iso-labels span {
      margin: 0 10px;
      opacity: 0.7;
    }
  </style>
</head>
<body>
  <div class="iso-dashboard">
    <div class="iso-screen">
      <div class="chart-box">
        <canvas id="pieChart"></canvas>
      </div>
      <div class="chart-box">
        <canvas id="barChart"></canvas>
      </div>
      <div class="chart-box">
        <canvas id="lineChart"></canvas>
      </div>
      <div class="chart-box">
        <canvas id="tableChart"></canvas>
      </div>
    </div>
    <div class="iso-labels">
      <span>DESIGN</span>
      <span>DEVELOPMENT</span>
      <span>DASHBOARD</span>
    </div>
  </div>

  <script>
    // Sample data
    const pieData = {
      labels: ['Green', 'Blue', 'Orange'],
      datasets: [{
        data: [40, 30, 30],
        backgroundColor: ['#4caf50', '#2196f3', '#ff9800']
      }]
    };

    const barData = {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      datasets: [{
        label: 'Revenue',
        data: [12000, 19000, 15000, 22000],
        backgroundColor: '#2196f3'
      }]
    };

    const lineData = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
      datasets: [{
        label: 'Users',
        data: [100, 200, 300, 250, 400],
        borderColor: '#ff9800',
        fill: false
      }]
    };

    const tableData = {
      labels: ['Product A', 'Product B', 'Product C'],
      datasets: [{
        label: 'Sales',
        data: [300, 500, 200],
        backgroundColor: '#4caf50'
      }]
    };

    // Chart options
    const options = { responsive: true, plugins: { legend: { position: 'bottom' } } };

    // Render charts
    new Chart(document.getElementById('pieChart'), { type: 'pie', data: pieData, options });
    new Chart(document.getElementById('barChart'), { type: 'bar', data: barData, options });
    new Chart(document.getElementById('lineChart'), { type: 'line', data: lineData, options });
    new Chart(document.getElementById('tableChart'), { type: 'bar', data: tableData, options });
  </script>
</body>
</html>
