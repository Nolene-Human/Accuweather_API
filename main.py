'''
credit to 
NeuralNine (https://www.youtube.com/watch?v=9P5MY_2i7K8&t=47s)

'''


import datetime as dt
import requests

def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit -32)* (5/9)
    return celsius
    

base_url="http://dataservice.accuweather.com/forecasts/v1/daily/1day/247035?" #this is just for Amberley

api_key="vj4GmLNRQGrvg3p8CffKuYoYRFgAnlJe"

url=base_url + "apikey=" +api_key

response=requests.get(url).json()

print(response)
