import requests

def get_weather(city_name, api_key):
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

        print(f"City: {city_name}")
        print(f"Weather: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed}m/s")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    API_KEY = "163b55a2a0eea45ef037e83e59c1bb1d"
    CITY_NAME = input("Enter city name: ")
    get_weather(CITY_NAME, API_KEY)