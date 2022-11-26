import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df_poke = pd.read_csv(Path.cwd().parents[1] / 'data/pokemon.csv')
df = pd.read_csv(Path.cwd().parents[1] / "data/v2/match.csv")
print(df_poke)
print(df)
battles_won = df['Winner'].value_counts()
print(battles_won)
def specific_pokemon(name: str):
    x = df_poke[df_poke['Name'] == name]['Name']
    poke_id = df_poke[df_poke['Name'] == name]['Id']
    print(poke_id)
    y = df[df['Winner'] == poke_id]
    print(y)

    plt.bar(x,y)
    plt.savefig('plots/relative_power.png')	#saves the figure in the present directory



if __name__ == '__main__':
    specific_pokemon('pikachu')