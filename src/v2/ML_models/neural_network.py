import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("../../../data/v1/battle_data.csv")

y = df.iloc[:, :1]
X = df.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)

# Original data
nn = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10, 15), random_state=1)
nn.fit(X_train, y_train)
pred = nn.predict(X_test)
score = nn.score(X_test, y_test)

# Normalized data
nn_norm = MLPClassifier(activation='logistic', solver='sgd', hidden_layer_sizes=(10, 15), random_state=1)
scaler = MinMaxScaler()
X_norm = scaler.fit_transform(X_train)
X_norm_test = scaler.fit_transform(X_test)

nn_norm.fit(X_norm, y_train)
pred_norm = nn_norm.predict(X_norm_test)
score_norm = nn_norm.score(X_norm_test, y_test)



if __name__ == "__main__":
    print("original", score)
    print("normalize", score_norm)
