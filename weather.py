import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Create parameters for the API request
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        
        response = requests.get(base_url, params=params)
        data = response.json()

       
        if response.status_code == 200:
            return data
        else:
            print("Error:", data['message'])
            return None

    except requests.RequestException as e:
        print("Request error:", e)
        return None

def display_weather(weather_data):
    # Extract relevant information from the API response
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']

    # Display weather information
    print(f"\nCurrent Weather in {weather_data['name']}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description}")

def main():
    print("Weather Forecast Application")

    # Get API key from OpenWeatherMap (sign up for a free account to get your API key)
    api_key = "API_KEY" #dont have

    # Prompt the user to enter the name of a city or a zip code
    location = input("Enter the name of a city or a zip code: ")

    # Make the API request and get weather data
    weather_data = get_weather(api_key, location)

    # Display weather information to the user
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
