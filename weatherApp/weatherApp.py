#!\usr\bin\python3

import requests
from bs4 import BeautifulSoup
import collections

WeatherReport = collections.namedtuple('WeatherReport', 
                                        ['condition', 'temperature', 'scale', 'location'])


def print_header():
    pass

def get_zipcode():
    zipcode = input("Please enter zipcode:" )
    return zipcode

def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)

    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None 

def get_weather_from_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')

    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    
    #reall necessary to repeat this 4 times?
    loc = clean_up_text(loc)
    condition = clean_up_text(condition)
    temp = clean_up_text(temp)
    scale = clean_up_text(scale)
    
    report = WeatherReport(location=loc, condition=condition, temperature=temp, scale=scale)

    return report


def clean_up_text(text : str):
    if not text:
        return text
    
    return text.strip()

def WeatherApp():
    #print the header
    html = get_html_from_web(get_zipcode())
	    
    #parse the html
    if html:
        report = get_weather_from_html(html)
    else:
        print("Could not connect")
    #display for the forecast
    
    print(report)

WeatherApp()

if "__name__" == "__main__":
    WeatherApp()
