"""Module providing a function printing python version.
    sign up in http://api.weatherapi.com for a free plan and get api key.
    temporary api key with my gmail account:  37b67a948798401795e103922241309
"""

import requests
import click


@click.command()
@click.option("--city_name", default="London")
def get_city_weather(city_name: str) -> None:
    """Function printing python version."""
    APIKEY = "37b67a948798401795e103922241309"
    URL = f"http://api.weatherapi.com/v1/current.json?key={APIKEY}&q={city_name}&aqi=no"

    response = requests.get(URL)
    weather_json = response.json()

    # print(weather_json)
    tempe = weather_json.get('current').get('temp_c')
    description = weather_json.get('current').get('condition').get('text')

    print("Today's weather in", city_name, 'is', description, 'and', tempe, 'degrees.')
    print("Have a good", description, 'day')


if __name__ == "__main__":
    get_city_weather()
