import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Token_user'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = {'trainer_id': '28712'}

def test_ststus_code ():
    response = requests.get(url = f'{URL}/trainers', params = TRAINER_ID, headers = HEADER)
    assert response.status_code == 200

def test_part_of_response ():
    response_get = requests.get(url = f'{URL}/trainers', params = TRAINER_ID, headers = HEADER)
    assert response_get.json()['data'][0]['trainer_name'] == 'Tima'


