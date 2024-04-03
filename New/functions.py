import requests

def get_weather_from_api(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    reponse = requests.get(complete_url)

    return reponse.json()


def get_weather(city_name):

    api_key = "33b06f2a67c48ab5f654928116f7ac6d"
    weather_data = get_weather_from_api(api_key, city_name)

    if weather_data["cod"] == 401:
        print('Problema durante a requisição')
    elif weather_data["cod"] != '404':
        main_weather = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"]
        print(f"Clima em {city_name}: {main_weather}")
        print(f"Temperatura: {temperature - 273.15:.2f} graus")

    else:
        print("Cidade não encontrada!")
