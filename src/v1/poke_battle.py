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


def weinell_battle(first: int, second: int):
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

    diff_hp = poke_one.HP - poke_two.HP
    diff_attack = poke_one.Attack - poke_two.Attack
    diff_defense = poke_one.Defense - poke_two.Defense
    diff_sp_attack = poke_one.Sp_Attack - poke_two.Sp_Attack
    diff_sp_defense = poke_one.Sp_Defense - poke_two.Sp_Defense
    diff_speed = poke_one.Speed - poke_two.Speed

    return poke_one_id, poke_one.Name, poke_one.HP, poke_one.Attack, poke_one.Defense, poke_one.Sp_Attack, poke_one.Sp_Defense, poke_one.Speed, poke_one.Sum_stats, poke_two_id, poke_two_id, poke_two.Name, poke_two.HP, poke_two.Attack, poke_two.Defense, poke_two.Sp_Attack, poke_two.Sp_Defense, poke_two.Speed, poke_two.Sum_stats, diff_hp, diff_attack, diff_defense, diff_sp_attack, diff_sp_defense, diff_speed


def weinell_test():
    poke_count = MAX_ID
    header = ['Poke_1_Id', 'Poke_1_Name', 'Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack',
              'Poke_1_Sp_Defense', 'Poke_1_Speed', 'Poke_1_Sum_Stats',
              'Poke_2_Id', 'Poke_2_Name', 'Poke_2_HP', 'Poke_2_Attack', 'Poke_2_Defense', 'Poke_2_Sp_Attack',
              'Poke_2_Sp_Defense', 'Poke_2_Speed', 'Poke_2_Sum_Stats',
              'Diff_HP', 'Diff_Attack', 'Diff_Defense', 'Diff_Sp_Attack', 'Diff_Sp_Defense', 'Diff_Speed',
              'Diff_Sum_Stats']

    with open("../../data/v1/match_weinell.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(poke_count):
            for j in range(poke_count):
                print(i, "vs", j)
                # +1 because we are going for Pokemon id and not index in array
                writer.writerow(weinell_battle(j + 1, i + 1))


def weinell_calc():
    start_time = time.time()
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match_weinell.csv")

    for index, row in battle_results.iterrows():
        diff = ()

    print(time.time() - start_time)


def calc_battles():
    start_time = time.time()
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    for index, row in battle_results.iterrows():
        first_pokemon = row["Poke_1"]
        second_pokemon = row["Poke_2"]
        winner = row["Winner"]

        poke_one = pokemons.loc[pokemons["Id"] == first_pokemon].values[:, 4][0]
        poke_two = pokemons.loc[pokemons["Id"] == second_pokemon].values[:, 4][0]
    print(time.time() - start_time)


def plot_types():
    pokemons = read_pokemon_data("../../data/pokemon.csv")

    plot = pokemons['Type_1'].value_counts().plot(kind="bar", title="Number based on first type")
    fig = plot.get_figure()
    fig.savefig("../../data/typesfig.png")


if __name__ == "__main__":
    # write_all_battles()
    # battle_pokemon(4, 25)
    calc_battles()

    # weinell_test()
    # weinell_calc()
    # plot_types()
