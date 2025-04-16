#!/usr/bin/env python3

"""We're starting work with APIs and I'm not sure how it's going to go"""

import requests


def availableShips(passengerCount):
    """Also I just want to say how much I hate that we're working with
    the Starwars API
    Nothing against the project just everything against Starwars."""

    url = "https://swapi.dev/api/starships/"
    ret_list = []

    # This is where I started to worry about pagination
    # I've decided to worry about it later

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data["results"]:
            try:
                passengers = int(ship["passengers"].replace(",", ""))
                ship_name = ship["name"]
            except ValueError:
                # ship_name = ship["name"]
                passengers = ship["passengers"].replace(",", "")
                passengers = 0

            if passengers >= passengerCount:
                ret_list.append(ship["name"])

        url = data["next"]

    return ret_list
