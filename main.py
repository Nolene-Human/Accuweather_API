'''
This Application will call the daily weather from AccuWeather API for Amberley

credit to NeuralNine (https://www.youtube.com/watch?v=9P5MY_2i7K8&t=47s) for calling API

'''


import datetime as dt
import requests

def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit -32)* (5/9)
    return celsius
    

base_url="http://dataservice.accuweather.com/forecasts/v1/daily/1day/" #this is just for Amberley

location_key="247035"

api_key="vj4GmLNRQGrvg3p8CffKuYoYRFgAnlJe"

url=base_url + location_key+ "?apikey=" +api_key

response=requests.get(url).json()

#print(response)
'''
daily_forecasts = response.get('DailyForecasts')
if daily_forecasts:
    for forecast in daily_forecasts:
        date = forecast.get('Date')
        temperature = forecast.get('Temperature')
        day = forecast.get('Day')
        night = forecast.get('Night')

        print(f"Date: {date}")
        print(f"Temperature: {temperature}")
        print(f"Day: {day}")
        print(f"Night: {night}")
        print("\n")
else:
    print("No daily forecasts available")
'''

#This code will get the temperature
daily_forecasts = response.get('DailyForecasts')
if daily_forecasts:
    for forecast in daily_forecasts:
        day=forecast.get('Day',{}).get('PrecipitationIntensity') +" " + forecast.get('Day',{}).get('PrecipitationType')
        date = forecast.get('Date')
        date = date.split('T')[0]  # Split the date at 'T' and take the first part
        temperature1 = forecast.get('Temperature', {}).get('Minimum').get('Value')
        minimum = int(convert_to_celsius(temperature1))
        temperature2=forecast.get('Temperature', {}).get('Maximum').get('Value')
        maximum = int(convert_to_celsius(temperature2))
        
        print(f'Your day will have ' + day)
        print(f"Date: {date}")
        print(f"Maximum Temperature: {maximum} / Minimum Temperature: {minimum}")
        
        print("\n")
else:
    print("No daily forecasts available")