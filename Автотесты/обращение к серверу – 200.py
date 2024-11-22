import requests

BASE_URL = 'http://mice.dsm.dev.thehead.ru'

def test_get_endpoint():
    response = requests.get(f'{BASE_URL}/auth')
    print(response)
    assert response.status_code == 200

test_get_endpoint()