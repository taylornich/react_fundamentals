# question 1 task 2

import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)

if response:
    data = response.json()

    name = data['name']
    abilities = [ability['ability']['name'] for ability in data['abilities']]

    print(f"Name: {name}")
    for ability in abilities:
        print(f"Ability: {ability}")

else:
    print("There was no information for this Pokemon in the API.")