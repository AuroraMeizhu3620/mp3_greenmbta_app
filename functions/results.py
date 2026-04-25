from functions.geocode_transform import geocode_transform
from functions.nearest_stop import nearest_stop
from functions.stop_name import stop_name
from functions.station_address import station_address
from functions.get_air_quality import get_air_quality
from functions.interpret_aqi import interpret_aqi

def results(location):
    # Step 1: Geocode user input
    coords = geocode_transform(location)
    if coords is None:
        return {
            "error": "We couldn’t find that location. Try something like 'Boston College' or a full address."
        }

    latitude, longitude = coords

    # Step 2: Find nearest stop coordinates
    stop_coords = nearest_stop(latitude, longitude)
    if stop_coords is None:
        return {
            "error": "No nearby MBTA stops found. Try a different location."
        }

    stop_latitude, stop_longitude = stop_coords

    # Step 3: Get stop name + address
    stop_name_value = stop_name(stop_latitude, stop_longitude)
    stop_address_value = station_address(stop_latitude, stop_longitude)

    # Step 4: Get AQI
    aqi = get_air_quality(latitude, longitude)
    aqi_result = interpret_aqi(aqi)

    # Step 5: Build result
    result = {
        "location_input": "...",
        "coordinates": {
            "latitude": ...,
            "longitude": ...
        },
        "stop": {
            "name": "...",
            "address": "...",
            "latitude": ...,
            "longitude": ...
        },
        "air_quality": {
            "aqi": ...,
            "level": "...",
            "message": "..."
        }
    }


print(results("Babson College"))