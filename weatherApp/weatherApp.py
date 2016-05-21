#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def print_header():
    pass

def get_zipcode():
    zipcode = input("Please enter zipcode:" )
    return zipcode

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def get_weather_from_html(html_doc):
	soup = BeautifulSoup(html_doc, 'html.parser')
	location = soup.find(id='location').find('h1').get_text()
	temperature = soup.find(id='curCond').find(class_='wx_value').get_text()
	#scale = 
	#condition = 
	print(temperature)

def WeatherApp():
    #print the header
    html = get_html_from_web(get_zipcode())
	    
    #parse the html
    get_weather_from_html(html)
    #display for the forecast

WeatherApp()

if "__name__" == "__main__":
    WeatherApp()
