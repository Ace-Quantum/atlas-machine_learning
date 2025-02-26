#!/usr/bin/env python3

"""Returns planets with sentient species"""

import requests


def sentientPlanets():
    """I don't even know what pagination refers to"""

    url = "https://swapi.dev/api/species/"
    planets = set()

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data["results"]:
            is_sentient = (
                species["classification"].lower() == "sentient"
                or species["designation"].lower() == "sentient"
            )

            if is_sentient and species["homeworld"]:
                homeworld_response = requests.get(species["homeworld"])
                homeworld_data = homeworld_response.json()
                planets.add(homeworld_data["name"])

        url = data["next"]

    return list(planets)
