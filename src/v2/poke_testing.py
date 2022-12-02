from sklearn.preprocessing import MinMaxScaler
from src.ApiToCsv import read_pokemon_data
from pathlib import Path
import pandas as pd
import numpy as np


def get_two_pokemon(first_pokemon: int, second_pokemon: int, normalize: bool):
    pokemons = read_pokemon_data(Path.cwd().parents[2] / 'data/pokemon.csv')
    battles = pd.read_csv(Path.cwd().parents[2] / "data/v2/battle_data.csv")

    battles_dummies1_1 = pd.get_dummies(battles.Poke_1_Type_1, prefix='Poke_1_Type_1')

    battles.drop(labels='Poke_1_Type_1', axis=1, inplace=True)

    battles_dummies1_2 = pd.get_dummies(battles.Poke_1_Type_2, prefix='Poke_1_Type_2')
    battles.drop(labels='Poke_1_Type_2', axis=1, inplace=True)

    battles_dummies2_1 = pd.get_dummies(battles.Poke_2_Type_1, prefix='Poke_2_Type_1')
    battles.drop(labels='Poke_2_Type_1', axis=1, inplace=True)

    battles_dummies2_2 = pd.get_dummies(battles.Poke_2_Type_2, prefix='Poke_2_Type_2')
    battles.drop(labels='Poke_2_Type_2', axis=1, inplace=True)

    battles_ohe = pd.concat([battles, battles_dummies1_1], axis=1)
    battles_ohe = pd.concat([battles_ohe, battles_dummies1_2], axis=1)
    battles_ohe = pd.concat([battles_ohe, battles_dummies2_1], axis=1)
    battles_ohe = pd.concat([battles_ohe, battles_dummies2_2], axis=1)

    battles_ohe.drop(battles_ohe.index[:], inplace=True)
    battles_ohe.drop(['Did_Poke1_Win'], axis=1, inplace=True)

    # Import all pokemon data
    # One hot encode
    # Filter by the two pokemon ID's
    # Drop ID

    pokemons = pokemons.drop(columns=["Is_Legendary", "Sum_stats"])
    pokemons = pd.concat([pokemons], axis=1)

    poke_one = pokemons[pokemons["Id"] == first_pokemon].values[:, 2:][0]
    poke_two = pokemons[pokemons["Id"] == second_pokemon].values[:, 2:][0]

    data = np.concatenate((poke_one, poke_two))

    header = ['Poke_1_Type_1', 'Poke_1_Type_2', 'Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack',
              'Poke_1_Sp_Defense', 'Poke_1_Speed', 'Poke_2_Type_1', 'Poke_2_Type_2', 'Poke_2_HP', 'Poke_2_Attack',
              'Poke_2_Defense', 'Poke_2_Sp_Attack', 'Poke_2_Sp_Defense', 'Poke_2_Speed']
    df = pd.DataFrame([data], columns=header)

    df_dummies1_1 = pd.get_dummies(df.Poke_1_Type_1, prefix='Poke_1_Type_1')

    df.drop(labels='Poke_1_Type_1', axis=1, inplace=True)

    df_dummies1_2 = pd.get_dummies(df.Poke_1_Type_2, prefix='Poke_1_Type_2')
    df.drop(labels='Poke_1_Type_2', axis=1, inplace=True)

    df_dummies2_1 = pd.get_dummies(df.Poke_2_Type_1, prefix='Poke_2_Type_1')
    df.drop(labels='Poke_2_Type_1', axis=1, inplace=True)

    df_dummies2_2 = pd.get_dummies(df.Poke_2_Type_2, prefix='Poke_2_Type_2')
    df.drop(labels='Poke_2_Type_2', axis=1, inplace=True)

    df_ohe = pd.concat([df, df_dummies1_1], axis=1)
    df_ohe = pd.concat([df_ohe, df_dummies1_2], axis=1)
    df_ohe = pd.concat([df_ohe, df_dummies2_1], axis=1)
    df_ohe = pd.concat([df_ohe, df_dummies2_2], axis=1)

    df_ohe = pd.concat([battles_ohe, df_ohe])

    df_ohe.fillna(0, inplace=True)

    print(df_ohe)

    # Normalize begin
    # todo This needs to return df_ohe as normalized data (is not done)
    if normalize:
        df_ohe = df_ohe.transpose()
        scaler = MinMaxScaler()
        transformed_data = scaler.fit_transform(df_ohe)
        print(transformed_data)
        transformed_data = transformed_data.transpose()
        return transformed_data

    return df_ohe
