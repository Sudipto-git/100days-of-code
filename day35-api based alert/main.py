import requests

# Use the 'forecast' endpoint instead of 'weather' to get a list of forecasts
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = "98948800e2d04aa23e398455fea54ebb"

# Fix the parameters dictionary - add missing comma and provide a value for 'cnt'
OWM_PARAMS = {
    "lat": 32.239632,
    "lon": 77.188713 ,
    "appid": OWM_API_KEY,
    "units": "metric",  # Added comma here
    "cnt": 12  # Number of forecast timestamps (12 = 36 hours with 3-hour steps)
}

# Remove duplicate api_key definition
# api_key = "98948800e2d04aa23e398455fea54ebb"  

try:
    response = requests.get(OWM_ENDPOINT, params=OWM_PARAMS)
    response.raise_for_status()
    weather_data = response.json()

    will_rain = False
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if condition_code < 700:
            will_rain = True
            print(f"Bring an umbrella - Rain expected at {hour_data['dt_txt']}")
    
    if not will_rain:
        print("No umbrella needed for the next 36 hours")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
    
print(weather_data["list"][0]["weather"][0]["description"])