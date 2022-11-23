from src.ApiToCsv import read_pokemon_data


def get_two_pokemon(first_pokemon: int, second_pokemon: int):
    pokemons = read_pokemon_data("../../data/pokemon.csv")

    pokemons = pokemons.drop(columns=["Type_1", "Type_2", "Is_Legendary", "Sum_stats"])
    pokemons = pd.concat([pokemons], axis=1)

    poke_one = pokemons[pokemons["Id"] == first_pokemon].values[:, 2:][0]
    poke_two = pokemons[pokemons["Id"] == second_pokemon].values[:, 2:][0]

    data = np.concatenate((poke_one, poke_two))
    # print(f"My created pokemon {data}")

    df = pd.DataFrame([data])
    # print(f"df created pokemon {df}")
    return df
