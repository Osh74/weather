import requests
import json
import streamlit as st

# Display a headline at the top of the page
st.title("Real Time Weather")

# Access API key from Streamlit secrets
API_K = st.secrets["api_key"]  # Access to secret

# Streamlit input for city name
city_name = st.text_input("Please enter a city name for getting the current weather in it:")

# Define the function to get weather data
def weather_by_city(city_name, api_key):
    # Base URL for the API request
    base_url = "http://api.weatherapi.com/v1/current.json?"
    complete_url = base_url + "key=" + api_key + "&q=" + city_name

    # Get request to the API
    response = requests.get(complete_url)

    # Converting to JSON
    data = response.json()

    # Extracting data if the city is found
    if "error" not in data:
        current = data["current"]
        location = data["location"]

        # Extracting relevant fields
        temperature = current["temp_c"]
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind_speed = current["wind_kph"]

        # Display the weather data with bullets
        st.write(f"### Weather in {location['name']}, {location['country']}:")
        st.markdown(f"* **Temperature:** {temperature}°C")
        st.markdown(f"* **Description:** {condition}")
        st.markdown(f"* **Humidity:** {humidity}%")
        st.markdown(f"* **Wind speed:** {wind_speed} kph")
    else:
        # Display error if the city is not found
        st.error(f"City '{city_name}' not found.")

# If the user enters a city name, call the function to display the weather
if city_name:
    weather_by_city(city_name, API_K)
