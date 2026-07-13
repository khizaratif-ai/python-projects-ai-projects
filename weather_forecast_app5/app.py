from flask import Flask, render_template, request

import weather


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = None


    if request.method == "POST":

        city = request.form["city"]

        print("CITY ENTERED:", city)

        weather_data = weather.get_weather(city)

        print("WEATHER DATA:", weather_data)


    return render_template(
        "index.html",
        weather=weather_data
    )



if __name__ == "__main__":

    app.run(debug=True)