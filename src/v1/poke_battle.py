import csv
import time
from src.ApiToCsv import read_pokemon_data, read_battles_data
import numpy as np

MAX_ID = 151


def battle_pokemon(first: int, second: int):
    df = read_pokemon_data("../../data/pokemon.csv")
    poke_one = df[df["Id"] == first]
    poke_two = df[df["Id"] == second]

    poke_one_id = df[df["Id"] == first].values[:, 0][0]
    poke_two_id = df[df["Id"] == second].values[:, 0][0]

    poke_one_stats = poke_one["Sum_stats"].values[0]
    poke_two_stats = poke_two["Sum_stats"].values[0]

    if poke_one_stats > poke_two_stats:
        winner = poke_one_id
    else:
        winner = poke_two_id

    return poke_one_id, poke_two_id, winner


def write_all_battles():
    poke_count = MAX_ID
    header = ['Poke_1', 'Poke_2', 'Winner']

    with open("../../data/v1/match.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(poke_count):
            for j in range(poke_count):
                print(i, "vs", j)
                # +1 because we are going for Pokemon id and not index in array
                writer.writerow(battle_pokemon(j + 1, i + 1))


def calc_battles():
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    header = ['']

    for index, row in battle_results.iterrows():
        first_pokemon = row["Poke_1"]
        second_pokemon = row["Poke_2"]
        

        poke_one = pokemons[pokemons["Id"] == first_pokemon]
        poke_two = pokemons[pokemons["Id"] == second_pokemon]
        
        # HP,Attack,Defense,Sp_Attack,Sp_Defense,Speed

        poke_one_obj = {
            "poke_one_health": poke_one['HP'].values[0],
            "poke_one_attack": poke_one['Attack'].values[0],
            "poke_one_defense": poke_one['Defense'].values[0],
            "poke_one_spattack": poke_one['Sp_Attack'].values[0],
            "poke_one_spdefense": poke_one['Sp_Defense'].values[0],
            "poke_one_speed": poke_one['Speed'].values[0]
        }
        

        poke_two_obj = {
            "poke_two_health": poke_two['HP'].values[0],
            "poke_two_attack": poke_two['Attack'].values[0],
            "poke_two_defense": poke_two['Defense'].values[0],
            "poke_two_spattack": poke_two['Sp_Attack'].values[0],
            "poke_two_spdefense": poke_two['Sp_Defense'].values[0],
            "poke_two_speed": poke_two['Speed'].values[0]
        }


        winner = row["Winner"].values[0]

    return poke_one_obj, poke_two_obj







if __name__ == "__main__":

    calc_battles()
