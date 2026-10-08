import os
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / "API.env")


class DistanceService:
    GEOCODE_URL = "https://api.heigit.org/pelias/v1/search"
    MATRIX_URL = "https://api.heigit.org/openrouteservice/v2/matrix/driving-car"

    def __init__(self):
        self.headers = {
            'Authorization': os.getenv('API_KEY'),
            'Content-Type': 'application/json'
        }

    def get_coords_by_name(self, name):
        params = {
            "text": name
        }

        response = requests.get(DistanceService.GEOCODE_URL, headers=self.headers, params=params)
        data = response.json()
        return data['features'][0]['geometry']['coordinates']

    def get_distance(self, origin, destination):
        body = {
            "locations" : [origin, destination],
            "metrics" : ["distance"]
        }
        response = requests.post(DistanceService.MATRIX_URL, headers=self.headers, json=body)
        data = response.json()
        return data['distances']




