from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from pathlib import Path
from src.v2.poke_testing import get_two_pokemon

df = pd.read_csv(Path.cwd().parents[2] / "data/v2/battle_data.csv")

df_dummies1_1 = pd.get_dummies(df.Poke_1_Type_1, prefix='Poke_1_Type_1')
df.drop(labels='Poke_1_Type_1',axis=1, inplace=True)

df_dummies1_2 = pd.get_dummies(df.Poke_1_Type_2, prefix='Poke_1_Type_2')
df.drop(labels='Poke_1_Type_2',axis=1, inplace=True)

df_dummies2_1 = pd.get_dummies(df.Poke_2_Type_1, prefix='Poke_2_Type_1')
df.drop(labels='Poke_2_Type_1',axis=1, inplace=True)

df_dummies2_2 = pd.get_dummies(df.Poke_2_Type_2, prefix='Poke_2_Type_2')
df.drop(labels='Poke_2_Type_2',axis=1, inplace=True)

df_ohe = pd.concat([df, df_dummies1_1], axis=1)
df_ohe = pd.concat([df_ohe, df_dummies1_2], axis=1)
df_ohe = pd.concat([df_ohe, df_dummies2_1], axis=1)
df_ohe = pd.concat([df_ohe, df_dummies2_2], axis=1)

y = df_ohe.iloc[:, :1]
X = df_ohe.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X_train)
X_norm_test = scaler.fit_transform(X_test)

model_norm = Perceptron()
model_norm.fit(X_norm, y_train)
score_norm = model_norm.score(X_norm_test, y_test)

model = Perceptron()
model.fit(X_train, y_train)
preds = model.predict(X_test)
score = model.score(X_test, y_test)


if __name__ == "__main__":
    print("original", score)
    print("normalize", score_norm)
    battle = get_two_pokemon(1, 7)
    predict_battle = model.predict(battle)
    print(predict_battle)
