import csv
import time
from src.api_file_handler import read_pokemon_data, read_battles_data, write_battle
import numpy as np
import pandas as pd

MAX_ID = 151


def battle_pokemon():
    df = read_pokemon_data("../../data/pokemon.csv")
    for i in df.index:
        for j in df.index:

            poke_one = df[df["Id"] == i]
            poke_two = df[df["Id"] == j]

            poke_one_id = df[df["Id"] == i].values[:, 0][0]
            poke_two_id = df[df["Id"] == j].values[:, 0][0]

            poke_one_stats = poke_one["Sum_stats"].values[0]
            poke_two_stats = poke_two["Sum_stats"].values[0]

            if poke_one_stats > poke_two_stats:
                winner = poke_one_id
            else:
                winner = poke_two_id
            

            write_battle(poke_one_id, poke_two_id, winner)
            



def calc_battles():
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    header = ['Poke_1_Id', 'Poke_1_Name', 'Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack',
              'Poke_1_Sp_Defense', 'Poke_1_Speed', 'Poke_1_Sum_Stats',
              'Poke_2_Id', 'Poke_2_Name', 'Poke_2_HP', 'Poke_2_Attack', 'Poke_2_Defense', 'Poke_2_Sp_Attack',
              'Poke_2_Sp_Defense', 'Poke_2_Speed', 'Poke_2_Sum_Stats',
              'Diff_HP', 'Diff_Attack', 'Diff_Defense', 'Diff_Sp_Attack', 'Diff_Sp_Defense', 'Diff_Speed',
              'Diff_Sum_Stats']
    
    pokemon_list = []

    df = pd.DataFrame(columns=header)
    print(df)

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

    return df







if __name__ == "__main__":
    battle_pokemon()
 #   calc_battles()
