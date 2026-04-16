from pathlib import Path
import os
import requests
from dotenv import load_dotenv

load_dotenv()


# linking to API keys stored in .env file
MAPBOX_TOKEN = os.getenv("MAPBOX_API_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")






def nearest_stop(latitude, longitude):
    """
    Takes latitude and longitude and returns the nearest MBTA stop using the MBTA API."""
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]=0.05&sort=distance&page[limit]=1"

    try:
        data = requests.get(url).json()

        if len(data["data"]) == 0:
            print("Please try another location for your search.")
            return None

        stop = data["data"][0]["attributes"]

        description = stop["description"]
        municipality = stop["municipality"]
        wheelchair = stop["wheelchair_boarding"]

        return description

    except:
        print("Error: Could not find the nearest MBTA stop.")
        return None

result = nearest_stop(latitude, longitude)
print(result)


# returns the address of the stop using the name of the train station stop
def stop_address(description):
    """
    Takes the description of the nearest MBTA stop, which is a stop name, and returns the address of the stop using the Mapbox Geocoding API.
    """
    mapbox_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{description}.json?access_token={MAPBOX_TOKEN}&limit=1"
    try:
        data = requests.get(mapbox_url).json()
        if len(data["features"]) == 0:
            print("Error: Could not geocode the stop address.")
            return None
        address = data["features"][0]["place_name"]
        return address
    except:
        print("Error: Could not geocode the stop address.")
        return None

print(stop_address(result))


def stop_render(address):
    """
    Takes the address of the nearest MBTA stop and returns a URL to a static map image of the stop location using the Mapbox Static Images API.
    """
    mapbox_url = f"https://api.mapbox.com/styles/v1/mapbox/streets-v11/static/{address}/400x400?access_token={MAPBOX_TOKEN}"
    return mapbox_url


# attains AQI that describes the air quality
def get_air_quality(latitude, longitude):
    """
    Takes latitude and longitude and returns air quality (US AQI)
    from Open-Meteo Air Quality API.
    """

    air_url = f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longitude}&current=us_aqi"

    try:
        data = requests.get(air_url).json()

        aqi = data["current"]["us_aqi"]

        return aqi

    except:
        print("Error: Could not get air quality data.")
        return None

# Helper function to convert AQI value to a label
def air_quality_label(aqi):
    if aqi is None:
        return "Unavailable"
    elif aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"
    
aqi = get_air_quality(latitude, longitude)
label = air_quality_label(aqi)

print("AQI:", aqi)
print("Air Quality:", label)

# # def build_trip_info(place_name):
# #     """
# #     Combines all helper functions into one pipeline.
# #     """
# #     coordinates = geocode_place(place_name)
# #     if coordinates is None:
# #         return None

# #     latitude, longitude = coordinates

# #     nearest_stop = find_nearest_stop(latitude, longitude)
# #     air_quality = get_air_quality(latitude, longitude)

# #     return {
# #         "searched_place": place_name,
# #         "latitude": latitude,
# #         "longitude": longitude,
# #         "nearest_stop": nearest_stop,
# #         "air_quality": air_quality
# #     }


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