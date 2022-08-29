# import requests
# from pprint import pprint
# from datetime import datetime
#
#
# def weather():
#     parameters = {
#         'appid': '137d62f3c460fac41edca5930e84af7c',
#         'units': 'metric',
#         'lang': 'ru'
#     }
#     data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
#     temp = data['main']['temp']
#     description = data['weather'][0]['description']
#     wind = data['wind']['speed']
#     timezone = data['timezone']
#     sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime('%H:%M:%S')
#     sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime('%H:%M:%S')
#
#
