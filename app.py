from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace with your OpenWeatherMap API key
API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city:
        complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            weather_data = {
                "city": city,
                "temperature": data['main']['temp'],
                "description": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed']
            }
            return jsonify(weather_data)
        else:
            return jsonify({"error": "City not found"}), 404
    else:
        return jsonify({"error": "City not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)