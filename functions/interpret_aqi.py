from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

def interpret_aqi(aqi):
    if aqi is None:
        return {
            "level": "No data",
            "message": "No air quality data available. The air is... a mystery today"
        }

    if 0 <= aqi <= 50:
        return {
            "level": "Good",
            "message": (
                "The air is clean and fresh. Very low levels of pollutants like PM2.5 and ozone. "
                "Your lungs are getting mostly pure oxygen — perfect for exercise, deep breaths, and being outdoors."
            )
        }

    elif 51 <= aqi <= 100:
        return {
            "level": "Moderate",
            "message": (
                "The air has a small amount of pollution — tiny particles and gases are present. "
                "Most people are fine, but if you’re sensitive, you might notice slight irritation when breathing deeply."
            )
        }

    elif 101 <= aqi <= 150:
        return {
            "level": "Unhealthy for Sensitive Groups",
            "message": (
                "Pollutants like fine particles (PM2.5) are building up in the air. "
                "These can enter deep into the lungs. People with asthma or heart conditions "
                "may feel discomfort — consider limiting long outdoor activities."
            )
        }

    elif 151 <= aqi <= 200:
        return {
            "level": "Unhealthy",
            "message": (
                "The air contains high levels of harmful pollutants. "
                "Fine particles and ozone can irritate your lungs and reduce oxygen efficiency. "
                "Even healthy people may feel coughing or fatigue — outdoor activity is not recommended."
            )
        }

    elif 201 <= aqi <= 300:
        return {
            "level": "Very Unhealthy",
            "message": (
                "The air is heavily polluted. Tiny particles can pass into your bloodstream through the lungs. "
                "This can stress your heart and respiratory system. Stay indoors and avoid exertion."
            )
        }

    elif 301 <= aqi <= 500:
        return {
            "level": "Hazardous",
            "message": (
                "The air is dangerously polluted. High concentrations of toxic particles and gases. "
                "Breathing this air is harmful even for short periods — avoid going outside if possible."
            )
        }

    else:
        return {
            "level": "Invalid",
            "message": "AQI value is out of expected range."
        }