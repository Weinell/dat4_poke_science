import csv
from src.ApiToCsv import read_pokemon_data, read_battles_data
import pandas as pd
from pathlib import Path

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
        skip_pokemon = 0
        for i in range(poke_count):
            for j in range(poke_count):
                # Ignores itself  and
                if i != j and j > skip_pokemon:
                    # +1 because we are going for Pokemon id and not index in array
                    writer.writerow(battle_pokemon(i + 1, j + 1))
            skip_pokemon = skip_pokemon+1


def calc_stat_diff(poke1, poke2):
    return poke1 - poke2


def did_1_win(winner, first_poke):
    if winner == first_poke:
        return 1
    else:
        return 0


def calc_battles_diff():
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    df_diff = pd.DataFrame()

    header = ['Did_Poke1_Win','Hp_diff','Attack_diff','Defense_diff','Sp_Attack_diff','Sp_Defense_diff','Speed_diff']

    for index, row in battle_results.iterrows():
        first_pokemon = row["Poke_1"]
        second_pokemon = row["Poke_2"]

        winner = row["Winner"]

        poke_one = pokemons[pokemons["Id"] == first_pokemon]
        poke_two = pokemons[pokemons["Id"] == second_pokemon]

        win = did_1_win(winner, first_pokemon)

        hp_diff = calc_stat_diff(poke_one['HP'].values[0],poke_two['HP'].values[0])
        attack_diff = calc_stat_diff(poke_one['Attack'].values[0],poke_two['Attack'].values[0])
        defense_diff = calc_stat_diff(poke_one['Defense'].values[0],poke_two['Defense'].values[0])
        sp_attack_diff = calc_stat_diff(poke_one['Sp_Attack'].values[0],poke_two['Sp_Attack'].values[0])
        sp_defense_diff = calc_stat_diff(poke_one['Sp_Defense'].values[0],poke_two['Sp_Defense'].values[0])
        speed_diff = calc_stat_diff(poke_one['Speed'].values[0],poke_two['Speed'].values[0])

        battle_diff = pd.Series([win, hp_diff, attack_diff, defense_diff, sp_attack_diff, sp_defense_diff, speed_diff])

        battle_to_concat_diff = pd.DataFrame([battle_diff])
        df_diff = pd.concat([battle_to_concat_diff, df_diff], ignore_index=True)

    df_diff.to_csv('battle_data_diff.csv', index=False, header=header)


def calc_battles():
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    header = ['Did_Poke1_Win','Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack','Poke_1_Sp_Defense','Poke_1_Speed','Poke_2_HP', 'Poke_2_Attack', 'Poke_2_Defense', 'Poke_2_Sp_Attack','Poke_2_Sp_Defense', 'Poke_2_Speed']

    df = pd.DataFrame()

    for index, row in battle_results.iterrows():
        first_pokemon = row["Poke_1"]
        second_pokemon = row["Poke_2"]

        winner = row["Winner"]

        poke_one = pokemons[pokemons["Id"] == first_pokemon]
        poke_two = pokemons[pokemons["Id"] == second_pokemon]

        win = did_1_win(winner, first_pokemon)

        pokemon_battle_info = pd.Series([win,poke_one['HP'].values[0],poke_one['Attack'].values[0],poke_one['Defense'].values[0],poke_one['Sp_Attack'].values[0],poke_one['Sp_Defense'].values[0],poke_one['Speed'].values[0],poke_two['HP'].values[0],poke_two['Attack'].values[0],poke_two['Defense'].values[0],poke_two['Sp_Attack'].values[0],poke_two['Sp_Defense'].values[0],poke_two['Speed'].values[0]])
        battle_to_concat = pd.DataFrame([pokemon_battle_info])
        df = pd.concat([battle_to_concat, df], ignore_index=True)

    df.to_csv('battle_data.csv', index=False, header=header)


if __name__ == "__main__":
    #print(battle_pokemon(1, 9))
    write_all_battles()
