import requests
from pprint import pprint

pokemon_number = input("What is the pokemon ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)
pokemon = response.json()

print(response) #shows the response code
"""
print(response)

pprint(pokemon)
"""

moves = pokemon['moves']
for move in moves:
    print(move['move']['name'])
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])

