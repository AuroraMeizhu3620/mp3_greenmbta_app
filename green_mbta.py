from pathlib import Path
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# linking to API keys stored in .env file
MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# geocode_transform: user address input -> (geocode_transform) -> latitude and longtitude
def geocode_transform(place):
    """
    Takes place name or address entered by user and returns it in the latitude and longitude format using the Mapbox Geocoding API.
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json?access_token={MAPBOX_TOKEN}&limit=1"

    try:
        data = requests.get(url).json()

        # if no results found
        if len(data["features"]) == 0:
            print("Error: Could not geocode the place. Please check your input and try again.")
            return None

        longitude = data["features"][0]["center"][0]
        latitude = data["features"][0]["center"][1]

        return latitude, longitude

    except: # Check this later
        print("Error: Could not geocode the place. Please check your input and try again.")
        return None

print(geocode_transform("1234432tgfdvqv"))

# def find_nearest_stop(latitude, longitude):
#     """
#     Takes latitude and longitude and returns the nearest MBTA stop name.
#     """
#     url = "https://api-v3.mbta.com/stops"

#     params = {
#         "api_key": MBTA_API_KEY,
#         "filter[latitude]": latitude,
#         "filter[longitude]": longitude,
#         "sort": "distance",
#         "page[limit]": 1
#     }

#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     data = response.json()

#     stops = data.get("data", [])
#     if not stops:
#         return None

#     stop = stops[0]
#     stop_name = stop["attributes"]["name"]

#     return stop_name


# def get_air_quality(latitude, longitude):
#     """
#     Takes latitude and longitude and returns air quality information
#     from Open-Meteo Air Quality API.
#     """
#     url = "https://air-quality-api.open-meteo.com/v1/air-quality"

#     params = {
#         "latitude": latitude,
#         "longitude": longitude,
#         "current": "us_aqi"
#     }

#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     data = response.json()

#     current_data = data.get("current", {})
#     us_aqi = current_data.get("us_aqi")

#     return us_aqi


# def build_trip_info(place_name):
#     """
#     Combines all helper functions into one pipeline.
#     """
#     coordinates = geocode_place(place_name)
#     if coordinates is None:
#         return None

#     latitude, longitude = coordinates

#     nearest_stop = find_nearest_stop(latitude, longitude)
#     air_quality = get_air_quality(latitude, longitude)

#     return {
#         "searched_place": place_name,
#         "latitude": latitude,
#         "longitude": longitude,
#         "nearest_stop": nearest_stop,
#         "air_quality": air_quality
#     }


# def main():
#     place_name = input("Enter a place name or address: ")

#     result = build_trip_info(place_name)

#     if result is None:
#         print("Could not find that location.")
#     else:
#         print("\nResult:")
#         print(f"Place: {result['searched_place']}")
#         print(f"Latitude: {result['latitude']}")
#         print(f"Longitude: {result['longitude']}")
#         print(f"Nearest MBTA stop: {result['nearest_stop']}")
#         print(f"US AQI: {result['air_quality']}")


# if __name__ == "__main__":
#     main()