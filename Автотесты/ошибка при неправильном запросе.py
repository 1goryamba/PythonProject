import requests


def test_bad_request():
    url = 'https://www.sadurala.com/catalog/plodovye-derevia?page=123'
    response = requests.get(url)
    print(response)
    assert response.status_code == 404


test_bad_request()