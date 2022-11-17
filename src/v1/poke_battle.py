import csv
from src.ApiToCsv import read_pokemon_data

MAX_ID = 151


def battle_pokemon(first: int, second: int):
    df = read_pokemon_data()
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


if __name__ == "__main__":
    write_all_battles()
    #battle_pokemon(4, 25)
