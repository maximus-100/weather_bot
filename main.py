import requests
import datetime
from pprint import pprint
from config import *


def get_weather(city, open_weather_token):

    code_to_smaile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облочно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000023A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data['weather'][0]['main']
        if weather_description in code_to_smaile:
            wd = code_to_smaile[weather_description]
        else:
            wd = 'Посмотри в окноб не пойму что там происходит!'

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f'***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}***\n'
              f'Погода в городе: {city}\nТемпература: {cur_weather}С° {wd}\n'
              f'Влажность: {humidity}%\nДавления: {pressure} мм.рт.ст\nВетер: {wind} м/с\n'
              f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n'
              f'Хорошого дня!'
              )

    except Exception as ex:
        print(ex)
        print("Проверте названия города")


def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()