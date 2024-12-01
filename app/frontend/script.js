function getWeather() {
  fetch('/api/weather')
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").innerText = `Clima atual: ${data.temperature}°C, ${data.condition}`;
    })
    .catch(error => {
      document.getElementById("output").innerText = "Erro ao obter o clima.";
      console.error(error);
    });
}

function getForecast() {
  fetch('/api/forecast')
    .then(response => response.json())
    .then(data => {
      document.getElementById("output").innerText = `Previsão: ${data.forecast}`;
    })
    .catch(error => {
      document.getElementById("output").innerText = "Erro ao obter a previsão.";
      console.error(error);
    });
}
