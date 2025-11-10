import os
import requests
import json
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
        'q': None, 
        'limit': 1, 
        'appid': API_KEY
    }

    # Params required for weather api call
    weather_params = {
        'lat': None, 
        'long': None, 
        'appid': API_KEY,
        'units': 'metric'
    }

    @classmethod
    def get_location(cls, location):
        
        # Set location param to given city 
        cls.location_params['q'] = location

        try:
            # Send API call for given city - stores result as a list of dictionaries
            location_request = requests.get(cls.location_url, params=cls.location_params, timeout=5)
            
            # Check for error status codes
            location_request.raise_for_status()

            location_response = location_request.json()

            # Get dictionary from the list
            location_data = location_response[0]

            lat = location_data['lat']
            lon = location_data['lon']

        except requests.exceptions.Timeout:
            print("Error: The request timed out.")

        except requests.exceptions.HTTPError as e:
            print(f"Error: A server error occurred: {e}")

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the server. Check your internet.")

        except json.JSONDecodeError:
            print("Error: Failed to decode the server's response.")

        except (IndexError, KeyError):
            print("Error: Could not find location data in the response.")

        except Exception as e:
            print(f"An unknown error occurred: {e}")
                    
        return (lat, lon)
    
    @classmethod 
    def get_weather(cls, coords):
        
        # Configure weather params
        cls.weather_params['lat'] = coords[0]
        cls.weather_params['lon'] = coords[1]

        try:
            weather_request = requests.get(cls.weather_url, cls.weather_params, timeout=5)

            weather_request.raise_for_status()

            weather_response = weather_request.json()
        except requests.exceptions.Timeout:
            print("Error: The request timed out.")

        except requests.exceptions.HTTPError as e:
            print(f"Error: A server error occurred: {e}")

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the server. Check your internet.")

        except json.JSONDecodeError:
            print("Error: Failed to decode the server's response.")

        except (IndexError, KeyError):
            print("Error: Could not find location data in the response.")

        except Exception as e:
            print(f"An unknown error occurred: {e}")

        print(f"The temperature in {weather_response['name']}, {weather_response['sys']['country']} is {int(weather_response['main']['temp'])}°C")


if __name__ == "__main__":
    
    weather_client = WeatherClient()
    
    while True:
        city = input('Enter a city: ')
        
        weather_client.get_weather(weather_client.get_location(city))
    


    

    