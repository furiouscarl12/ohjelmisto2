#teht1

import requests

print(requests.get('https://api.chucknorris.io/jokes/random').json()['value'])