from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '77db77152109a773eccd59b6080822ad'

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form["city"]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                "city": city.title(),
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            error_message = "City not found. Please try again."

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
