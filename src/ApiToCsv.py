import requests


def get_pokemon(name: str):
    res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    
    data = res.json()

    types = data['types']

    type1 = data['types'][0]
    type2 = data['types'][1] if len(data['types'])>1 else None


    hp = data['stats'][0]
    attack = data['stats'][1]
    defense = data['stats'][2]
    sp_attack = data['stats'][3]
    sp_defense = data['stats'][4]
    speed = data['stats'][5]

    print(type1)
    print(type2)

    

if __name__ == '__main__':
    get_pokemon('pikachu')
    get_pokemon('charizard')
