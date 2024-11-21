import requests

def get_weather(city, api_key):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.
    
    Args:
        city (str): The city name.
        api_key (str): Your OpenWeatherMap API key.
        
    Returns:
        dict: Weather data or an error message.
    """
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
