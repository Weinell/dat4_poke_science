from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("../../../data/v1/battle_data.csv")

y = df.iloc[:, :1]
X = df.iloc[:, 1:]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

score = knn.score(X_test, y_test)


if __name__ == "__main__":
    print(score)
