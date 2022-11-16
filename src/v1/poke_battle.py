import csv
import math
import os.path
import random
import pandas as pd
from src.ApiToCsv import read_pokemon_data
#hej
MAX_ID = 151

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
        winner = poke_one.values[0]
        loser = poke_two.values[0]
        stat_diff = poke_one_stats - poke_two_stats
    else:
        winner = poke_two.values[0]
        loser = poke_one.values[0]
        stat_diff = poke_two_stats - poke_one_stats

    return winner, loser, stat_diff


def write_all_battles():
    poke_count = MAX_ID
    header = ['Winner', 'Loser', 'stat_diff']

    with open("../../data/v1/match.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(poke_count):
            for j in range(poke_count):
                print(i, "vs", j)
                writer.writerow(battle_pokemon(j + 1, i + 1))


if __name__ == "__main__":
    write_all_battles()

