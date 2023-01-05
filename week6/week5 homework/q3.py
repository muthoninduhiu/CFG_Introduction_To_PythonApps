"""
Question 3
In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
retrieve multiple Pokemon and save their names and moves to a file.
Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
Pokemon. Save their names and moves into a file called 'pokemon.txt'
"""
import requests

pokemon_list = [1, 25, 133, 4, 7, 150]
with open('pokemon.txt', 'w+') as pokemon_file:
    # Then in a for loop call the API to retrieve the data for each pokemon
    for my_pokemon in pokemon_list:

        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(my_pokemon)
        response = requests.get(url)
        print(response)

        pokemon = response.json()

        pokemon_file.write(f"name: {pokemon['name']}'\n")

        pokemon_file.write("moves: \n")

        moves = pokemon['moves']
        for move in moves:
            pokemon_file.write(f" - {move['move']['name']}\n")
