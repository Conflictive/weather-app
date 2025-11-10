# 🌦️ Command-Line Weather App

A simple Python application that fetches the current weather for any city, built to practice API usage


## Features
* Fetches real-time weather data from the [OpenWeatherMap](https://openweathermap.org/) API.
* Geocoding: Converts a city name (like "London") into coordinates.
* Robust error handling for bad inputs, network failures, and API errors.
* Secure API key management using a `.env` file.

## Tech Used
* Python
* `requests` (for API calls)
* `python-dotenv` (for environment variables)

## How to Run
1.  Clone this repository:
    `git clone [your-github-repo-url]`
2.  Create and activate a virtual environment:
    `python -m venv .venv`
    `.\.venv\Scripts\activate`
3.  Install the required packages:
    `pip install -r requirements.txt`
4.  Sign up for a free API key at [OpenWeatherMap.org](https://openweathermap.org/).
5.  Create a `.env` file and add your key:
    `API_KEY=your_key_here`
6.  Run the application:
    `python main.py`