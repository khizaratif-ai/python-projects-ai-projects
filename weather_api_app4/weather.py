import requests
import config


def get_weather(city):

    url = (
        "https://api.weatherapi.com/v1/current.json?"
        f"key={config.API_KEY}&"
        f"q={city}"
    )

    response = requests.get(url)

    data = response.json()


    if "error" in data:
        return None


    weather = {

        "city": data["location"]["name"],

        "country": data["location"]["country"],

        "temperature": data["current"]["temp_c"],

        "condition": data["current"]["condition"]["text"],

        "humidity": data["current"]["humidity"],

        "wind": data["current"]["wind_kph"]

    }


    return weather