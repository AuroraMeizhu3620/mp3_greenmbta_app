from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# linking to API keys stored in .env file
MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# geocode_transform: user address input -> (geocode_transform) -> latitude and longtitude
def geocode_transform(place):
    """
    Takes place name or address entered by user and returns it in the latitude and longitude format using the Mapbox Geocoding API.
    """
    mapbox_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token={MAPBOX_TOKEN}&limit=1"

    try:
        data = requests.get(mapbox_url).json()

        # if no results found
        if len(data["features"]) == 0:
            print("Error: Could not geocode the place. Please check your input and try again.")
            return None

        longitude = data["features"][0]["center"][0]
        latitude = data["features"][0]["center"][1]

        return (latitude, longitude)

    except: # If anything else were to be the case
        print("Error: Could not geocode the place. Please check your input and try again.")
        return None