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

    df = pd.DataFrame([data])

    return df
