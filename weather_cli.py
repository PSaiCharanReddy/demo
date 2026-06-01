#!/usr/bin/env python3
"""
Weather CLI App
Usage: python weather_cli.py <city>
"""
import sys
import requests

API_KEY = "45fabab81b9413c8d5a1fc21b2fde3a7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city."""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(data):
    """Display weather information in a formatted way."""
    if not data:
        return

    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print(f"\n{'='*50}")
    print(f"Weather in {city}, {country}")
    print(f"{'='*50}")
    print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"Conditions: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"{'='*50}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather_cli.py <city>")
        print("Example: python weather_cli.py London")
        sys.exit(1)

    city = ' '.join(sys.argv[1:])
    print(f"Fetching weather for {city}...")

    weather_data = get_weather(city)
    if weather_data:
        display_weather(weather_data)
    else:
        print("Failed to retrieve weather data. Please check the city name and try again.")

if __name__ == "__main__":
    main()
