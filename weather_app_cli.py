from datetime import datetime
from weather_app.api import get_weather

def display_weather(data):
    """
    Displays weather details in the console.
    
    Args:
        data (dict): The weather data.
    """
    if data and data.get("cod") == 200:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')
        
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
    elif "error" in data:
        print(f"Error: {data['error']}")
    else:
        print("City not found. Please check the name and try again.")

def cli_mode(api_key):
    """
    Command-line interface for the Weather App.
    
    Args:
        api_key (str): Your OpenWeatherMap API key.
    """
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            break
        weather_data = get_weather(city, api_key)
        display_weather(weather_data)
