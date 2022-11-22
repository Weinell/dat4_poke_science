from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

df = pd.read_csv("battle_data.csv")

y = df.iloc[:, :1]
X = df.iloc[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


rfc = RandomForestClassifier(n_estimators=500)
model = rfc.fit(X_train, y_train)

pred = model.predict(X_test)




if __main__ == '__main__':
    print(f"accuracy: {accuracy_score(pred, y_test)}")
