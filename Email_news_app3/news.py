import requests
import config


def get_news(topic):

    url = (
        "https://newsapi.org/v2/everything?"
        f"q={topic}&"
        "sortBy=publishedAt&"
        "language=en&"
        f"apiKey={config.API_KEY}"
    )


    response = requests.get(url)

    data = response.json()


    articles = data["articles"]


    news = ""


    for article in articles[:5]:

        title = article["title"]

        description = article["description"]


        news += f"""
{title}

{description}

---------------------

"""


    return news