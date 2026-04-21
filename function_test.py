from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# linking to API keys stored in .env file
MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# geocode_transform: user address input -> (geocode_transform) -> latitude and longitude
from functions.geocode_transform import geocode_transform
latitude, longitude = geocode_transform("Babson College")


# start latitude, longitude -> (nearest_stop) -> nearest MBTA stop, latitude, longitude
from functions.nearest_stop import nearest_stop
stop_name, stop_latitude, stop_longitude = nearest_stop(latitude, longitude)


# latitude, longitutde -> (get_air_quality) -> air quality information at where you are going to the train station from
from functions.get_air_quality import get_air_quality
aqi = get_air_quality(latitude, longitude)


# AQI value -> (interpret_aqi) -> AQI level and message
from functions.interpret_aqi import interpret_aqi
print(interpret_aqi(aqi))

# # def main():
# #     place_name = input("Enter a place name or address: ")

# #     result = build_trip_info(place_name)

# #     if result is None:
# #         print("Could not find that location.")
# #     else:
# #         print("\nResult:")
# #         print(f"Place: {result['searched_place']}")
# #         print(f"Latitude: {result['latitude']}")
# #         print(f"Longitude: {result['longitude']}")
# #         print(f"Nearest MBTA stop: {result['nearest_stop']}")
# #         print(f"US AQI: {result['air_quality']}")


# # if __name__ == "__main__":
# #     main()