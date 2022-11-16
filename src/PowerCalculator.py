import pandas as pd


data = './data/pokemon.csv'
df = pd.read_csv(data)
print(df)


print(df.columns)

def sum_stats():
    for index in df.index:
        df['Sum_Stats'] = df.apply(lambda row: row.HP + row.Attack + row.Defense + row.SpAttack + row.SpDefense + row.Speed,axis=1)

sum_stats()
print(df)

