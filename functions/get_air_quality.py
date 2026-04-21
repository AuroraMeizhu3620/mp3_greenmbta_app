from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def get_air_quality(latitude, longitude):
    """
    Takes latitude and longitude and returns air quality information
    from Open-Meteo Air Quality API.
    """
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "us_aqi"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    current_data = data.get("current", {})
    us_aqi = current_data.get("us_aqi")

    return us_aqi