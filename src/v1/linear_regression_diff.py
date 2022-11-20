import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import linear_model


df = pd.read_csv('battle_data_diff.csv')

X = df.iloc[:,1:]
y = df.iloc[:,:1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Scale data
SC = StandardScaler()
X_train = SC.fit_transform(X_train)
X_test = SC.transform(X_test)

# Ridge regression
reg = linear_model.Ridge(alpha=0.5)
reg.fit(X_train, y_train)

pred = reg.predict(X_test)
score = reg.score(X_test, y_test)

if __name__ == '__main__':
    print(reg.coef_)
    print(reg.intercept_)
    print('preds', pred)
    print('score', score)