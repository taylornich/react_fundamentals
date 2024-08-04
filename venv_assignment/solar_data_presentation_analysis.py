# Question 2 task 3

import requests


    
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies"

    response = requests.get(url)

    if response:
        data = response.json()
        planets = data['bodies']

        return [
            {
                'name': planet.get('englishName', 'Unknown'),
                'mass' : planet.get('mass', {}).get('massValue', 0),
                'orbit_period' : planet.get('orbitPeriod', 0)
            }
            for planet in planets if planet['isPlanet']
        ]
    else:
        print("Unable to retrieve data from the API.")

def find_heaviest_planet_data(planets):

    if not planets: 
        return('Unknown', 0)

    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if planet['mass'] > max_mass:
            max_mass = planet['mass']
            heaviest_planet = planet
    
    if heaviest_planet:
        return (heaviest_planet['name'], heaviest_planet['mass'])
    else:
        return ("Unknown", 0)

def main():

    planets = fetch_planet_data()

    if planets:
        name, mass = find_heaviest_planet_data(planets)
        print(f"The heaviest planet is {name} with a mass of {mass} kg.")


if __name__ == "__main__":
    main()



    