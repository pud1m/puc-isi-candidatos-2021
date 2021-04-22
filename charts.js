
const getYears = (payload) => {
  const list = [];
  payload.forEach(year => list.push(year.year));
  return list;
}
const getData = (payload, attr, subattr) => {
  const list = [];
  payload.forEach(year => list.push(year[attr][subattr]));
  return list;
}



// ============== Charts
document.addEventListener('DOMContentLoaded', () => {
  createChart1();
  createChart2();
  createChart3();
  createChart4();
});

const createChart1 = async () => {
  const ctx = document.getElementById('chart1').getContext('2d');

  const payload = results;
  const yearList = getYears(payload);
  const actualData = getData(payload, 'gender', 'women');

  const data = {
    labels: yearList,
    datasets: [{
      label: 'Porcentagem de candidaturas femininas',
      data: actualData,
    }]
  }
  
  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Candidaturas femininas, frente ao total de candidaturas (não há dados para 1996)'
        }
      },
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    },
  };

  const newChart = new Chart(ctx, config);
}

const createChart2 = async () => {
  const ctx = document.getElementById('chart2').getContext('2d');

  const payload = results;
  const yearList = getYears(payload);
  const actualData = getData(payload, 'gender', 'womenElected');

  const data = {
    labels: yearList,
    datasets: [{
      label: 'Porcentagem de eleitas que eram mulheres',
      data: actualData,
    }]
  }
  
  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Mulheres eleitas, frente ao total de pessoas eleitas (não há dados para 1996)'
        }
      },
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    },
  };

  const newChart = new Chart(ctx, config);
}

const createChart3 = async () => {
  const ctx = document.getElementById('chart3').getContext('2d');

  const payload = results;
  const yearList = getYears(payload);
  const actualData = getData(payload, 'avgAge', 'candidates');

  const data = {
    labels: yearList,
    datasets: [{
      label: 'Média da idade',
      data: actualData,
    }]
  }
  
  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Idade média dos candidatos'
        }
      },
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    },
  };

  const newChart = new Chart(ctx, config);
}

const createChart4 = async () => {
  const ctx = document.getElementById('chart4').getContext('2d');

  const payload = results;
  const yearList = getYears(payload);
  const actualData = getData(payload, 'avgAge', 'elected');

  const data = {
    labels: yearList,
    datasets: [{
      label: 'Média da idade',
      data: actualData,
    }]
  }
  
  const config = {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Idade média dos candidatos eleitos'
        }
      },
      scales: {
        y: {
          min: 0,
          max: 100
        }
      }
    },
  };

  const newChart = new Chart(ctx, config);
}