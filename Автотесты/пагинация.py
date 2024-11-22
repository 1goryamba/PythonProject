import requests

def test_pagination():
    page_number = 15
    per_page = 2
    query_params = {'page': page_number, 'per_page': per_page}
    url = 'http://mice.dsm.dev.thehead.ru/'
    response = requests.get(url, params=query_params)
    print(response)
    assert response.status_code == 200
    # results = response.json()
    # assert len(results) <= per_page

test_pagination()