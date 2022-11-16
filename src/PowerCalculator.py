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


### Version 1: 1v1 with sum of stats

### Version 2: 1v1 with sum of stats 
###            1 type

### Version 3: 1v1 with sum of stats
###            1 type
###            best physical attack

### Version 4: 1v1 with sum of stats
###            1 type
###            best special attack

### Version 5: 1v1 with sum of stats
###            2 type
###            best physical attack

### Version 6: 1v1 with sum of stats
###            2 type
###            best special attack
