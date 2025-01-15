from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city_name = request.form.get("city_name")
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

            weather_data = {
                "city": city_name,
                "weather": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }

        except requests.exceptions.RequestException as e:
            error = "Gagal mengambil data cuaca: " + str(e)
        except KeyError:
            error = "Nama kota tidak valid atau data tidak tersedia."

    return render_template("index.html", weather_data=weather_data, error=error)

if __name__ == "__main__":
    app.run(debug=True)