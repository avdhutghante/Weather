import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    """
    Get current weather for a city using OpenWeatherMap API.
    
    Args:
        city: Name of the city
        
    Returns:
        Weather information as a string
    """
    api_key = os.getenv("WEATHER_API_KEY")
    
    if not api_key:
        return "Weather API key not configured. Please add WEATHER_API_KEY to .env file"
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            
            return f"Weather in {city}: {temp}°C, feels like {feels_like}°C. Conditions: {description}. Humidity: {humidity}%"
        elif response.status_code == 404:
            return f"City '{city}' not found. Please check the spelling."
        else:
            return f"Unable to fetch weather data. Error code: {response.status_code}"
            
    except Exception as e:
        return f"Error fetching weather: {str(e)}"
