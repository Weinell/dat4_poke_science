import csv
import time
from src.ApiToCsv import read_pokemon_data, read_battles_data
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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
    start = time.time()
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    battle_results = read_battles_data("../../data/v1/match.csv")

    # header = ['Poke_1_Id', 'Poke_1_Name', 'Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack',
    #         'Poke_1_Sp_Defense', 'Poke_1_Speed', 'Poke_1_Sum_Stats',
    #         'Poke_2_Id', 'Poke_2_Name', 'Poke_2_HP', 'Poke_2_Attack', 'Poke_2_Defense', 'Poke_2_Sp_Attack',
    #         'Poke_2_Sp_Defense', 'Poke_2_Speed', 'Poke_2_Sum_Stats']
    # 'Diff_HP', 'Diff_Attack', 'Diff_Defense', 'Diff_Sp_Attack', 'Diff_Sp_Defense', 'Diff_Speed', 'Diff_Sum_Stats'

    header = ['Winner', 'Poke_1_HP', 'Poke_1_Attack', 'Poke_1_Defense', 'Poke_1_Sp_Attack', 'Poke_1_Sp_Defense',
              'Poke_1_Speed', 'Poke_2_HP', 'Poke_2_Attack', 'Poke_2_Defense', 'Poke_2_Sp_Attack', 'Poke_2_Sp_Defense',
              'Poke_2_Speed']

    df = pd.DataFrame()

    le1 = LabelEncoder()
    df1 = le1.fit_transform(pokemons["Type_1"])
    le2 = LabelEncoder()
    df2 = le2.fit_transform(pokemons["Type_1"])

    df1 = pd.DataFrame(data=df1)
    df2 = pd.DataFrame(data=df2)

    pokemons = pokemons.drop(columns=["Type_1", "Type_2"])
    pokemons = pd.concat([pokemons, df1, df2], axis=1)

    data = []

    for index, row in battle_results.iterrows():
        first_pokemon = row["Poke_1"]
        second_pokemon = row["Poke_2"]

        winner = row["Winner"]

        poke_one = pokemons[pokemons["Id"] == first_pokemon].values[:, 2:][0]
        poke_two = pokemons[pokemons["Id"] == second_pokemon].values[:, 2:][0]

        # diff = (poke_one - poke_two)[:6]
        con = np.concatenate((poke_one, poke_two))

        if winner == first_pokemon:
            con = np.append(con, [0])
        else:
            con = np.append(con, [1])

        data.append(con)
        """
        pokemon_battle_info = pd.Series(
            [winner, poke_one['HP'].values[0], poke_one['Attack'].values[0], poke_one['Defense'].values[0],
             poke_one['Sp_Attack'].values[0], poke_one['Sp_Defense'].values[0], poke_one['Speed'].values[0],
             poke_two['HP'].values[0], poke_two['Attack'].values[0], poke_two['Defense'].values[0],
             poke_two['Sp_Attack'].values[0], poke_two['Sp_Defense'].values[0], poke_two['Speed'].values[0]])
        battle_to_concat = pd.DataFrame([pokemon_battle_info])

        df = pd.concat([battle_to_concat, df], ignore_index=True)
        """
        # print('columns:', df.columns)
        # print(df)

    # print(df)
    # df.to_csv('battle_data.csv', index=False, header=header)
    # print(df)

    data = np.asarray(data)

    X = data[:, :-1].astype(int)
    y = data[:, -1].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=34)

    rfc = RandomForestClassifier(n_estimators=500)
    model = rfc.fit(X_train, y_train)

    pred = model.predict(X_test)

    print(f"accuracy: {accuracy_score(pred, y_test)}")
    print(f"execution in sec: {time.time() - start}")



if __name__ == "__main__":
    calc_battles()
