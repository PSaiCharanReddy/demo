#!/usr/bin/env python3
"""
Weather GUI App using tkinter
"""
import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "45fabab81b9413c8d5a1fc21b2fde3a7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Lookup")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Configure colors
        self.bg_color = "#2c3e50"
        self.fg_color = "#ecf0f1"
        self.button_color = "#3498db"

        self.root.configure(bg=self.bg_color)

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="Weather Lookup",
            font=("Helvetica", 20, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title.pack(pady=20)

        # City input frame
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)

        tk.Label(
            input_frame,
            text="Enter City:",
            font=("Helvetica", 12),
            bg=self.bg_color,
            fg=self.fg_color
        ).pack(side=tk.LEFT, padx=5)

        self.city_entry = tk.Entry(
            input_frame,
            font=("Helvetica", 12),
            width=20
        )
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind('<Return>', lambda e: self.get_weather())

        # Search button
        search_btn = tk.Button(
            self.root,
            text="Get Weather",
            font=("Helvetica", 12, "bold"),
            bg=self.button_color,
            fg=self.fg_color,
            command=self.get_weather,
            cursor="hand2",
            relief=tk.FLAT,
            padx=20,
            pady=5
        )
        search_btn.pack(pady=10)

        # Results frame
        self.results_frame = tk.Frame(self.root, bg=self.bg_color)
        self.results_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.result_label = tk.Label(
            self.results_frame,
            text="",
            font=("Helvetica", 11),
            bg=self.bg_color,
            fg=self.fg_color,
            justify=tk.LEFT
        )
        self.result_label.pack()

    def get_weather(self):
        city = self.city_entry.get().strip()

        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name")
            return

        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }

        try:
            response = requests.get(BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            self.display_weather(data)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch weather data:\n{str(e)}")
            self.result_label.config(text="")

    def display_weather(self, data):
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        result_text = f"""
Location: {city}, {country}

Temperature: {temp}°C
Feels Like: {feels_like}°C

Conditions: {description.capitalize()}
Humidity: {humidity}%
Wind Speed: {wind_speed} m/s
        """

        self.result_label.config(text=result_text)

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
