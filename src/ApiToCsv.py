import requests
import csv


def get_all_pokemon(limit: int):

    res = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset=0')
    data = res.json()

    return data['results']


def get_pokemon(id: int):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    res_legendary = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/{id}')
    
    data = res.json()

    name = data['name']
    poke_id = data['id']

    type1 = data['types'][0]['type']['name']
    type2 = data['types'][1]['type']['name'] if len(data['types'])>1 else None

    hp = data['stats'][0]['base_stat']
    attack = data['stats'][1]['base_stat']
    defense = data['stats'][2]['base_stat']
    sp_attack = data['stats'][3]['base_stat']
    sp_defense = data['stats'][4]['base_stat']
    speed = data['stats'][5]['base_stat']

    is_legendary = True if res_legendary.json()['is_legendary'] | res_legendary.json()['is_mythical'] else False

    return poke_id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed, is_legendary


def convert_pokemon_to_csv():
    
    header = ['Id', 'Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Sp. Attack', 'Sp. Defense', 'Speed', 'Is_Legendary']
    # data = [poke_id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed]

    all_pokemon = get_all_pokemon(9999)

    with open('./data/pokemon.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)


        for index, i in enumerate(all_pokemon):
            pokemon = get_pokemon(index + 1)
            writer.writerow(pokemon)
            print(pokemon)


if __name__ == '__main__':
    convert_pokemon_to_csv()
