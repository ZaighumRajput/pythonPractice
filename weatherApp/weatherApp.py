#!/usr/bin/python3
import requests

def print_header():
    pass

def get_zipcode():
    zipcode = input("Please enter zipcode:" )
    return zipcode

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def WeatherApp():
    #print the header
    html = get_html_from_web(get_zipcode())
    print(html)
    #get html from web
    #parse the html
    #display for the forecast

WeatherApp()

if "__name__" == "__main__":
    WeatherApp()
