import requests
import json
import streamlit as st

API_K=st.secrets["api_key"] #Access to secret

city_name=input("Please enter a city name for getting the current weather in it: ")

def weatherֹ_by_city(city_name, api_key):

    #Base + complete url for the API request
    base_url="http://api.weatherapi.com/v1/current.json?"
    complete_url=base_url + "key=" + API_K + "&q=" + city_name

    #Get request to the API
    response=requests.get(complete_url)

    #Converting to JSON
    data=response.json()

    #Erxtacrting data if city was found
    if "error" not in data:
        current=data["current"]
        location=data["location"]

        #Extracting relevant fields
        temperature=current["temp_c"]
        condition=current["condition"]["text"]
        humidity=current["humidity"]
        wind_speed=current["wind_kph"]

        # Display the weather data
        print(f"Weather in {location['name']}, {location['country']}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} kph")
    else:
        print(f"City '{city_name}' not found.")

# Call the function to get weather data
weatherֹ_by_city(city_name, API_K)
