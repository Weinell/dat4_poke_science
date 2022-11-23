from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from src.poke_testing import get_two_pokemon
import pandas as pd
import numpy as np



df = pd.read_csv("battle_data.csv")

y = df.iloc[:, :1]
X = df.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rfc = RandomForestClassifier(n_estimators=3)
model = rfc.fit(X_train, y_train)

predict_against_testset = model.predict(X_test)

pokemons_to_battle = get_two_pokemon(150, 4)
predict_two_pokemon = model.predict(pokemons_to_battle)


if __name__ == "__main__":
    print(predict_two_pokemon)
