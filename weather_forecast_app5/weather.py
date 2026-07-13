import requests
import config


def get_weather(city):

    url = (
        "https://api.weatherapi.com/v1/forecast.json?"
        f"key={config.API_KEY}&"
        f"q={city}&"
        "days=5"
    )

    response = requests.get(url)

    data = response.json()

    print(data)   # remove later after testing


    if "error" in data:
        return None


    weather = {

        "city": data["location"]["name"],

        "country": data["location"]["country"],

        "temperature": data["current"]["temp_c"],

        "condition": data["current"]["condition"]["text"],

        "icon": data["current"]["condition"]["icon"],

        "humidity": data["current"]["humidity"],

        "wind": data["current"]["wind_kph"],

        "feels": data["current"]["feelslike_c"],

        "forecast": []

    }


    for day in data["forecast"]["forecastday"]:

        weather["forecast"].append({

            "date": day["date"],

            "temperature": day["day"]["avgtemp_c"],

            "condition": day["day"]["condition"]["text"],

            "icon": day["day"]["condition"]["icon"]

        })


    return weather