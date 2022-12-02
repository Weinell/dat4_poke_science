from pathlib import Path
import requests
import csv
import pandas as pd


def read_pokemon_data(file_path: Path | str):
    if not Path(file_path).is_file():
        print('File did not exist', file_path)
        convert_pokemon_to_csv()

    df = pd.read_csv(file_path)
    df['Type_2'] = df['Type_2'].fillna("noType")
    return df


def read_battles_data(file_path: Path | str):
    df = pd.read_csv(file_path)
    return df


def get_all_pokemon(limit: int):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=0')
    data = res.json()

    return data['results']


def get_pokemon(poke_id: int):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke_id}')
    res_legendary = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{poke_id}')

    data = res.json()

    name = data['name']
    poke_id = data['id']

    type1 = data['types'][0]['type']['name']
    type2 = data['types'][1]['type']['name'] if len(data['types']) > 1 else None

    hp = data['stats'][0]['base_stat']
    attack = data['stats'][1]['base_stat']
    defense = data['stats'][2]['base_stat']
    sp_attack = data['stats'][3]['base_stat']
    sp_defense = data['stats'][4]['base_stat']
    speed = data['stats'][5]['base_stat']
    stats_sum = hp + attack + defense + sp_attack + sp_defense + speed

    is_legendary = True if res_legendary.json()['is_legendary'] | res_legendary.json()['is_mythical'] else False

    return poke_id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, stats_sum, is_legendary,


def convert_pokemon_to_csv():
    header = ['Id', 'Name', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Attack', 'Sp_Defense', 'Speed',
              'Sum_stats',
              'Is_Legendary']
    # data = [poke_id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed]

    all_pokemon = get_all_pokemon(151)

    with open(Path.cwd().parents[2] / 'data/pokemon.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for index, i in enumerate(all_pokemon):
            pokemon = get_pokemon(index + 1)
            writer.writerow(pokemon)
            print(pokemon)


if __name__ == '__main__':
    convert_pokemon_to_csv()
