# question 2 task 2

import requests

def fetch_planet_data():

    url = "https://api.le-systeme-solaire.net/rest/bodies"

    response = requests.get(url)

    if response:
        data = response.json()
        planets = data['bodies']


        for planet in planets:
            if planet['isPlanet']:
                name = planet.get('englishName', 'Unknown')
                mass = planet.get('mass', {}).get('massValue', 'Unknown')
                orbit_period = planet.get('orbitPeriod', 'Unknown')

                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

    else:
        print("Data for planet not found in the Solar System API.")


fetch_planet_data()