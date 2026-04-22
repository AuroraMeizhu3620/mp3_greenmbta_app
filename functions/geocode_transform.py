import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")

def geocode_transform(place):
    """
    Takes a place name or address and returns (latitude, longitude)
    using the Mapbox Geocoding API.
    """
    print("MAPBOX_API_KEY loaded:", bool(MAPBOX_TOKEN))

    if not MAPBOX_TOKEN:
        print("Error: MAPBOX_API_KEY is missing.")
        return None

    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1
    }

    try:
        response = requests.get(url, params=params)
        print("Mapbox status code:", response.status_code)

        data = response.json()
        print("Mapbox response:", data)

        if "features" not in data or len(data["features"]) == 0:
            print("Error: Could not geocode the place. Please check your input and try again.")
            return None

        longitude = data["features"][0]["center"][0]
        latitude = data["features"][0]["center"][1]

        return latitude, longitude

    except Exception as e:
        print("Error during geocoding:", e)
        return None