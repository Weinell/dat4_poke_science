from src.ApiToCsv import read_pokemon_data
from pathlib import Path
import pandas as pd
import numpy as np


def get_two_pokemon(first_pokemon: int, second_pokemon: int):
    pokemons = read_pokemon_data(Path.cwd().parents[2] / 'data/pokemon.csv')

    pokemons = pokemons.drop(columns=["Type_1", "Type_2", "Is_Legendary", "Sum_stats"])
    pokemons = pd.concat([pokemons], axis=1)

    poke_one = pokemons[pokemons["Id"] == first_pokemon].values[:, 2:][0]
    poke_two = pokemons[pokemons["Id"] == second_pokemon].values[:, 2:][0]

    data = np.concatenate((poke_one, poke_two))

    header = ['Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack', 'Poke_1_Sp_Defense', 'Poke_1_Speed', 'Poke_2_HP', 'Poke_2_Attack','Poke_2_Defense', 'Poke_2_Sp_Attack', 'Poke_2_Sp_Defense','Poke_2_Speed']

    df = pd.DataFrame([data],columns=header)

    return df
