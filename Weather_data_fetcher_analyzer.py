#!/usr/bin/env python
# coding: utf-8

# In[6]:


#TASK 4 -
#10c7518a894f01ff1df9d928eaa25289
#importing libraries 
import requests
import csv
from datetime import datetime
#entering API key from the website
API_KEY='10c7518a894f01ff1df9d928eaa25289'
TARGET_CITY = 'Tokyo' 
#Setting the name of the log file
LOG_FILE = 'weather_data.csv' 

#Fetches live weather data from OpenWeatherMap
def fetch_weather(city: str, api_key: str) -> dict:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' # Gets temperature in Celsius
    }
    
    try:
        #Simple request with general error handling
        response = requests.get(BASE_URL, params=params, timeout=10)
        
        if response.status_code != 200:
            print(f"[ERROR] API failed with status code {response.status_code}. Check key or city.")
            return {}
            
        return response.json()
        
    except requests.exceptions.RequestException as e:
        # Handles all common network/connection errors
        print(f"[ERROR] Network problem occurred: {e}")
        return {}

#Analyzes data and returns a summary string with alerts
def analyze_weather(weather_data: dict) -> str:
    # if data is bad
    if not weather_data or 'main' not in weather_data:
        return "Analysis Failed."

    # Direct access is simpler than .get() 
    temp_celsius = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data.get('wind', {}).get('speed', 0)
    
    #Temperature Summary 
    if temp_celsius <= 10:
        temp_summary = "Cold (≤10°C)"
    elif temp_celsius <= 24: # This covers 10.01 to 24
        temp_summary = "Mild (11-24°C)"
    else: # This covers 25 and up
        temp_summary = "Hot (≥25°C)"

    #Warnings/Alerts
    alerts = []
    
    if wind_speed > 10: 
        alerts.append("High wind alert!")
        
    if humidity > 80: 
        alerts.append("Humid conditions!")
        
    full_summary = temp_summary
    if alerts:
        # Putting the summary and alerts together neatly
        full_summary += f" | Alerts: {' | '.join(alerts)}"

    return full_summary

#Fetches, analyzes, and appends the data to a simple CSV file
def log_weather(city: str, filename: str):
    print(f"\nStarting Simple Log Process for {city} ")
    weather_data = fetch_weather(city, API_KEY)
    
    # Stop if fetch failed
    if not weather_data:
        return 
        
    analysis_summary = analyze_weather(weather_data)
    
    # data extraction for the log file
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind = weather_data.get('wind', {}).get('speed', 'N/A')
    description = weather_data['weather'][0]['description']
    
    log_entry = [timestamp, city, f"{temp:.2f}", humidity, wind, description, analysis_summary]
    csv_header = ['Timestamp', 'City', 'Temp_C', 'Humidity_%', 'Wind_Speed', 'Description', 'Analysis']

    try:
        # Open in 'a' (append) mode.
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Simple header logic: Write the header every time (simple method).
            writer.writerow(csv_header) 
            
            writer.writerow(log_entry)
            
        print(f"Data successfully logged to {filename}.")
        print(f"Summary: {analysis_summary}")
        
    except IOError as e:
        print(f"\n[ERROR] Could not write to file {filename}: {e}")


if __name__ == "__main__":
    log_weather(TARGET_CITY, LOG_FILE)


# In[ ]:




