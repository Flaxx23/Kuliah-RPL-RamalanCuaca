import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city_name = city_entry.get()
    api_key = "163b55a2a0eea45ef037e83e59c1bb1d"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        result = (
            f"City: {city_name}\n"
            f"Weather: {weather}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind_speed}m/s\n"
        )
        
        result_label.config(text=result)
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", str(e))
    except KeyError as e:
        messagebox.showerror("Error", f"Invalid data: {e}")

# Setup GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("300x400")
root.configure(bg="#f0f8ff")  # Warna background yang segar

title_label = tk.Label(root, text="Weather App", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#ff4500")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 12), bg="#f0f8ff")
city_label.pack(pady=5)

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12, "bold"), command=get_weather, bg="#ff4500", fg="#ffffff")
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f8ff")
result_label.pack(pady=10)

root.mainloop()