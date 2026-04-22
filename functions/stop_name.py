from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

# linking to API keys stored in .env file
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# start (latitude, longitude) -> (nearest MBTA stop, latitude, longitude)
def stop_name(latitude, longitude):
    url = f"https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]=0.05&sort=distance&page[limit]=1"

    try:
        data = requests.get(url).json()

        if len(data["data"]) == 0:
            print("Please try another location for your search.")
            return None

        stop = data["data"][0]["attributes"]

        stop_name = stop["name"]

        return stop_name

    except:
        print("Error: There is no MBTA stop within 3.45 miles (0.05 degrees) of the location you entered. Please try another location for your search.")
        return None