import pandas as pd
from pathlib import Path
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Original data
nn = MLPClassifier(activation='relu', solver='adam', hidden_layer_sizes=(8, 8, 8), max_iter=500)
nn.fit(X_train, y_train)
pred = nn.predict(X_test)
score = nn.score(X_test, y_test)

# Normalized data
nn_norm = MLPClassifier(activation='relu', solver='adam', hidden_layer_sizes=(8, 8, 8), max_iter=500)
scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X_train)
X_norm_test = scaler.fit_transform(X_test)

nn_norm.fit(X_norm, y_train)
pred_norm = nn_norm.predict(X_norm_test)
score_norm = nn_norm.score(X_norm_test, y_test)



if __name__ == "__main__":
    print("original", score)
    print("normalize", score_norm)