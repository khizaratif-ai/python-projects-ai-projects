import requests
from config import API_KEY

BASE_URL = "https://app.ticketmaster.com/discovery/v2/events.json"


def search_events(keyword):
    """
    Search for music events using the Ticketmaster Discovery API.
    Returns a list of event dictionaries.
    """

    params = {
        "apikey": API_KEY,
        "keyword": keyword,
        "classificationName": "music",
        "size": 20
    }

    events = []

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "_embedded" not in data:
            return events

        for event in data["_embedded"]["events"]:

            # Event Name
            name = event.get("name", "N/A")

            # Date
            date = event.get("dates", {}) \
                        .get("start", {}) \
                        .get("localDate", "N/A")

            # Time
            time = event.get("dates", {}) \
                        .get("start", {}) \
                        .get("localTime", "N/A")

            # Ticket URL
            ticket_url = event.get("url", "#")

            # Image
            image = ""
            if "images" in event and len(event["images"]) > 0:
                image = event["images"][0]["url"]

            # Venue & City
            venue = "Unknown Venue"
            city = "Unknown City"

            if "_embedded" in event:

                venues = event["_embedded"].get("venues", [])

                if venues:
                    venue = venues[0].get("name", "Unknown Venue")
                    city = venues[0].get("city", {}).get("name", "Unknown City")

            events.append({
                "name": name,
                "date": date,
                "time": time,
                "venue": venue,
                "city": city,
                "image": image,
                "url": ticket_url
            })

    except requests.exceptions.RequestException as e:
        print("Network Error:", e)

    except Exception as e:
        print("Error:", e)

    return events


# Test the file directly
if __name__ == "__main__":

    keyword = input("Search Artist: ")

    results = search_events(keyword)

    print(f"\nFound {len(results)} event(s)\n")

    for event in results:

        print("----------------------------------")
        print("Artist :", event["name"])
        print("Date   :", event["date"])
        print("Time   :", event["time"])
        print("Venue  :", event["venue"])
        print("City   :", event["city"])
        print("Ticket :", event["url"])