import requests

city = input("Input a city: ")

url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=aad40c0ed686e7682d0d4fe1fed34128"

response = requests.get(url).json()

lat = response[0]['lat']
lon = response[0]['lon']

url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=aad40c0ed686e7682d0d4fe1fed34128"
