import requests


def get_pokemon(name: str):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    
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

    return poke_id, name, type1, type2, hp, attack, defense, sp_attack, sp_defense, speed

    

if __name__ == '__main__':
    get_pokemon('pikachu')
    get_pokemon('charizard')
    print(get_pokemon('pikachu'))
