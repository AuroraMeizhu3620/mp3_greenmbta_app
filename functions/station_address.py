import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

def station_address(stop_latitude, stop_longitude):
    url = (
        f"https://api.mapbox.com/search/geocode/v6/reverse"
        f"?longitude={stop_longitude}"
        f"&latitude={stop_latitude}"
        f"&access_token={MAPBOX_API_KEY}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if "features" not in data or len(data["features"]) == 0:
            return "Address not available"

        feature = data["features"][0]
        properties = feature.get("properties", {})

        full_address = properties.get("full_address")
        name = properties.get("name")
        place_formatted = properties.get("place_formatted")

        if full_address:
            return full_address
        elif name and place_formatted:
            return f"{name}, {place_formatted}"
        elif name:
            return name
        else:
            return "Address not available"

    except Exception as e:
        print("Error finding station address:", e)
        return "Address not available"