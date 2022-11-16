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

    poke_one = df[df["Id"] == first]
    poke_two = df[df["Id"] == second]



    print(poke_one["Sum_stats"])
    print(poke_two["Sum_stats"])

    #poke_one.astype({"Sum_stats": "int"})
    
   #if poke_one.Sum_stats > poke_two.Sum_stats:
       # print(f"{poke_one} wins")
   #else:
       # print(f"{poke_two} wins")


if __name__ == "__main__":
    battle_pokemon(4, 25)