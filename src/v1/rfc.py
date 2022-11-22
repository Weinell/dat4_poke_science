from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

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


df = pd.read_csv("battle_data.csv")

y = df.iloc[:, :1]
X = df.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rfc = RandomForestClassifier(n_estimators=3)
model = rfc.fit(X_train, y_train)

pokemon_stats = get_two_pokemon(150, 4)

# apply
# decision_path
apply = model.apply(pokemon_stats)
dp = model.decision_path(pokemon_stats)

pred = model.predict(X_test)
pred2 = model.predict(pokemon_stats)


if __name__ == "__main__":
    print(pred2)

