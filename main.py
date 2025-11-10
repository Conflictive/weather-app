import os
import requests
import json
from dotenv import load_dotenv

load_dotenv() 
# Get API Key from .env file 
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file. Please check your setup.")

class WeatherClient():
    # Base url for geocode api calls
    location_url = 'http://api.openweathermap.org/geo/1.0/direct'

    # Base url for weather api calls
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'

    @classmethod
    def get_location(cls, location):
        
        # Set location param to given city 
        location_params = {
            'q': location, 
            'limit': 1, 
            'appid': API_KEY
        }

        try:
            # Send API call for given city - stores result as a list of dictionaries
            location_request = requests.get(cls.location_url, params=location_params, timeout=5)
            
            # Check for error status codes
            location_request.raise_for_status()

            location_response = location_request.json()

            # Get dictionary from the list
            location_data = location_response[0]

            lat = location_data['lat']
            lon = location_data['lon']

            return (lat, lon)

        except requests.exceptions.Timeout:
            print("Error: The request timed out.")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: A server error occurred: {e}")
            return None
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the server. Check your internet.")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to decode the server's response.")
            return None
        except (IndexError, KeyError):
            print("Error: Could not find location data in the response.")
            return None
        except Exception as e:
            print(f"An unknown error occurred: {e}")
            return None     
        
    @classmethod 
    def get_weather(cls, coords):
        
        lat, lon = coords
        
        # Configure weather params
        weather_params = {
            'lat': lat, 
            'lon': lon, 
            'appid': API_KEY,
            'units': 'metric'
        }

        try:
            weather_request = requests.get(cls.weather_url, params=weather_params, timeout=5)

            weather_request.raise_for_status()

            weather_response = weather_request.json()

            print(f"The temperature in {weather_response['name']}, {weather_response['sys']['country']} is {int(weather_response['main']['temp'])}°C")
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

if __name__ == "__main__":

    while True:
        city = input('Enter a city (or "q" to quit): ')
        if city.lower() == 'q':
            break
        
        coords = WeatherClient.get_location(city)
        
        if coords:
            WeatherClient.get_weather(coords)
    


    

    