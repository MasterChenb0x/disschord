#!/usr/local/bin/python3

import requests, json

def fahrenheit_convert(temp):
    """
    Converts Kelvin (thank you, openweathermap.org) into Fahrenheit.
    """
    # Formula: (kTemp - 273.15) * 9/5 + 32

    return ((temp - 273.15) * (9/5)) + 32

def get_weather(city):
    api_key = open("weathertoken.txt", "r").read().splitlines()
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key[0] + "&q=" + city

    response = requests.get(complete_url)

    x = response.json()

    if x['cod'] != "404":
        y = x['main']
        curr_temp = round(fahrenheit_convert(y['temp']), 2)
        curr_press = y['pressure']
        curr_humid = y['humidity']
        z = x['weather']
        weather_desc = z[0]['description']

        return f"The current temperature of {city} is {curr_temp}. {weather_desc}"
    else:
        return "City Not Found"

if __name__ == "__main__":
    print("This cannot be ran on its own. I mean, it can, but you won't like it.")
