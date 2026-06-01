#!/usr/bin/env python3
"""
Weather Web Server using Flask
Returns JSON weather data
"""
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "45fabab81b9413c8d5a1fc21b2fde3a7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Weather API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            h1 { color: #2c3e50; }
            .endpoint {
                background: white;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            code {
                background: #ecf0f1;
                padding: 2px 6px;
                border-radius: 3px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <h1>Weather API Server</h1>
        <p>Simple weather lookup API powered by OpenWeatherMap</p>

        <div class="endpoint">
            <h3>GET /weather</h3>
            <p><strong>Query Parameters:</strong></p>
            <ul>
                <li><code>city</code> - City name (required)</li>
            </ul>
            <p><strong>Example:</strong></p>
            <code>GET /weather?city=London</code>
        </div>

        <div class="endpoint">
            <h3>Response Format</h3>
            <pre>{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "description": "partly cloudy",
  "wind_speed": 3.5
}</pre>
        </div>
    </body>
    </html>
    """

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({
            'error': 'Missing required parameter: city',
            'usage': '/weather?city=<city_name>'
        }), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Format the response
        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed']
        }

        return jsonify(weather_info)

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return jsonify({'error': f'City not found: {city}'}), 404
        return jsonify({'error': f'API error: {str(e)}'}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Failed to fetch weather data: {str(e)}'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'service': 'weather-api'})

if __name__ == "__main__":
    print("Starting Weather API Server...")
    print("Access the API at: http://localhost:5000")
    print("Example: http://localhost:5000/weather?city=London")
    app.run(debug=True, host='0.0.0.0', port=5000)
