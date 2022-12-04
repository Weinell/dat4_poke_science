from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from pathlib import Path
from src.v1.poke_testing import get_two_pokemon

df = pd.read_csv(Path.cwd().parents[2] / 'data/v1/battle_data.csv')

y = df.iloc[:, :1]
X = df.iloc[:, 1:]

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
    battle = get_two_pokemon(490, 9)
    predict_battle = model.predict(battle)
    print(predict_battle)
