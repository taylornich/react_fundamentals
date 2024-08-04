# question 1 task 3

import requests

def fetch_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response = requests.get(url)

    if response:
        return response.json()
    else:
        print("There was no information in the API for this pokemon.")

def pokemon_average_weight(pokemon_list):

    total = 0

    for pokemon in pokemon_list:
        total += pokemon['weight']
    
    if pokemon_list:
        return total / len(pokemon_list) 
    else:
        return None

def main():
    pokemon_names = ['pikachu', 'bulbasaur', 'charmander']

    data_list = []

    for name in pokemon_names:
        data = fetch_data(name)
        if data:
            data_list.append(data)

            abilities = [ability['ability']['name'] for ability in data['abilities']]
            print(f"Name: {name}")
            for ability in abilities:
                print(f"Ability: {ability}")
                print()
    avg_weight = pokemon_average_weight(data_list)
    print(f"Average weight of the three Pokemon: {avg_weight: .2f}")


if __name__ == "__main__":
    main()