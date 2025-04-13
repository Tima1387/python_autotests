import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Token_user'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = {'trainer_id': '28712'}


create_pokemon = { "name": "generate","photo_id": -1 }
change_pokemon = {"pokemon_id": "286732","name": "New Name","photo_id": -1}
add_pokeball = {"pokemon_id": "286697"}


'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = create_pokemon)
print(response.text)'''

'''response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = change_pokemon) 
print(response.text)'''

'''response = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = add_pokeball)
print(response.text)'''

response_get = requests.get(url = f'{URL}/trainers', params = TRAINER_ID, headers = HEADER)
print(response_get.text)