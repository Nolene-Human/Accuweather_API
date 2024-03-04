import requests
import datetime as dt

# This API endpoint is connecting to AI Weather by Meteosource
url = "https://ai-weather-by-meteosource.p.rapidapi.com/daily"

querystring = {"place_id":"amberley-2193968","language":"en","units":"metric"}

headers = {
	"X-RapidAPI-Key": "288c14825emsh14cc91fddf688ecp1472e0jsn804504883645",
	"X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

today=dt.datetime.now()
today = str(today).split(' ')[0]  # Split the date at space to compare today's date
count =1

def print_daily_data(response):
    print ("This is the weather forecast for the next 21 days")

    count = 1

    for daily in response.json().get('daily').get('data'):
        print('This is day ' , count)
        date = (daily.get('day'))
        print(date)
        count += 1


def todays_weather(response):
    
    today = dt.datetime.now()
    today = str(today).split(' ')[0]  # Split the date at space to compare today's date
   

    for daily in response.json().get('daily').get('data'):
        date = (daily.get('day'))

        if today==date:
            print(daily.get('summary'))

        else:
            print("No forecast available")

