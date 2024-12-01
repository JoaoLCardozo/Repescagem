from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Habilita CORS

def fetch_weather_data():
    try:
        response = requests.get("https://api.weatherapi.com/v1/current.json?key=15db00a81ebf4b959d710415240112&q=London")
        response.raise_for_status()
        data = response.json()
        return {"temperature": data["current"]["temp_c"], "condition": data["current"]["condition"]["text"]}
    except requests.RequestException:
        return fetch_backup_weather_data()

def fetch_backup_weather_data():
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=51.51&longitude=-0.13&current_weather=true")
        response.raise_for_status()
        data = response.json()
        return {"temperature": data["current_weather"]["temperature"], "condition": "Desconhecido"}
    except requests.RequestException:
        return {"error": "Nenhuma API disponível"}

def fetch_forecast_data():
    try:
        response = requests.get("https://api.weatherapi.com/v1/forecast.json?key=15db00a81ebf4b959d710415240112&q=London&days=3")
        response.raise_for_status()
        data = response.json()
        return {"forecast": data["forecast"]["forecastday"][0]["day"]["condition"]["text"]}
    except requests.RequestException:
        return {"error": "Nenhuma API disponível"}

@app.route('/api/weather', methods=['GET'])
def get_weather():
    data = fetch_weather_data()
    return jsonify(data)

@app.route('/api/forecast', methods=['GET'])
def get_forecast():
    data = fetch_forecast_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
