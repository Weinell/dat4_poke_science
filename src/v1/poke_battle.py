import math
import os.path
import random
import pandas as pd
from src.ApiToCsv import read_pokemon_data

MAX_ID = 905


def get_random_pokemon(not_this_pokemon: int | None):
    poke_id = math.floor(random.random() * MAX_ID) + 1
    print(poke_id)


def battle_pokemon(first: int, second: int):
    df = read_pokemon_data()
    global winner
    global loser
    global stat_diff

    poke_one = df[df["Id"] == first]
    poke_two = df[df["Id"] == second]

    poke_one_stats = poke_one["Sum_stats"].values[0]
    poke_two_stats = poke_two["Sum_stats"].values[0]

    if poke_one_stats > poke_two_stats:
        winner = poke_one
        loser = poke_two
        stat_diff = poke_one_stats - poke_two_stats
    else:
        winner = poke_two
        loser = poke_one
        stat_diff = poke_two_stats - poke_one_stats

    return winner, loser, stat_diff


if __name__ == "__main__":
    battle_pokemon(3, 25)
