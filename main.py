import os
import requests
from dotenv import load_dotenv

load_dotenv() 
# Get API Key from .env file 
API_KEY = os.getenv("API_KEY")

class WeatherClient():
    # Base url for geocode api calls
    location_url = 'http://api.openweathermap.org/geo/1.0/direct'

    # Base url for weather api calls
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'

    # Params required by geocode api call 
    location_params = {
        'q': 'London', 
        'limit': 1, 
        'appid': API_KEY
    }

    # Params required for weather api call
    location_params = {
        'lat': None, 
        'long': None, 
        'appid': API_KEY
    }

    @classmethod
    def get_location(cls, location):
        
        # Set location param to given city 
        cls.location_params['q'] = location

        # Send API call for given city - stores result as a list of dictionaries
        location_response = requests.get(cls.location_url, params=cls.location_params).json()

        # Get dictionary from the list
        location_data = location_response[0]

        # Store latitude data from API call
        lat = location_data['lat']
        lon = location_data['lon']
        


if __name__ == "__main__":
    
    weather_client = WeatherClient()

    city = input('Enter a city: ')
    
    weather_client.get_location(city)
    


    

    