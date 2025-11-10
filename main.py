import os
import requests
from dotenv import load_dotenv

load_dotenv() 
# Get API Key from .env file 
API_KEY = os.getenv("API_KEY")

class Weather():
    pass

if __name__ == "__main__":
    print(API_KEY)
    


    

    