import pandas as pd


df = pd.read_csv('battle_data.csv')

X = df.iloc[:,1:]
y = df.iloc[:,:1]

if __name__ == '__main__':
    print(X)
    print(y)