# Weather Lookup Apps

Three implementations of a weather lookup application using Python.

## Setup

### 1. Python Environment (pyenv + venv)

```bash
# Python 3.10.11 is already installed via pyenv
pyenv version

# Virtual environment is already created
source venv/bin/activate

# Dependencies are already installed
pip list
```

### 2. Get API Key

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your free API key
3. Replace `your_api_key_here` in each Python file with your actual API key

## Applications

### 1. CLI App (`weather_cli.py`)

Command-line weather lookup tool.

**Usage:**
```bash
python weather_cli.py London
python weather_cli.py "New York"
python weather_cli.py Tokyo
```

**Features:**
- Simple command-line interface
- Displays temperature, conditions, humidity, and wind speed
- Error handling for invalid cities

### 2. GUI App (`weather_gui.py`)

Desktop application with tkinter interface.

**Usage:**
```bash
python weather_gui.py
```

**Features:**
- Clean graphical interface
- Text input for city name
- Button to fetch weather
- Displays formatted weather information
- Press Enter to search

### 3. Web Server (`weather_server.py`)

Flask-based REST API server.

**Usage:**
```bash
python weather_server.py
```

Then access:
- Home page: http://localhost:5000
- API endpoint: http://localhost:5000/weather?city=London
- Health check: http://localhost:5000/health

**Features:**
- RESTful API returning JSON
- Query parameter for city name
- HTML documentation page
- Error handling with appropriate HTTP status codes

**Example API Response:**
```json
{
  "city": "London",
  "country": "GB",
  "temperature": 15.5,
  "feels_like": 14.2,
  "humidity": 72,
  "description": "partly cloudy",
  "wind_speed": 3.5
}
```

## Testing

```bash
# Activate virtual environment
source venv/bin/activate

# Test CLI
python weather_cli.py London

# Test GUI (opens window)
python weather_gui.py

# Test Web Server
python weather_server.py
# In another terminal:
curl "http://localhost:5000/weather?city=London"
```

## Dependencies

- `requests` - HTTP library for API calls
- `flask` - Web framework for the server
- `tkinter` - GUI framework (included with Python)

## Notes

- All apps use metric units (Celsius, m/s)
- Free API tier has rate limits (60 calls/minute)
- API key must be added to each file before use
# demo
