import requests

auth_url = 'https://calendar.dev.thehead.ru/back-api/api/auth'
login_data = {
    'email': 'test2@example.com',
    'password': 'password',
    'Authorization' : 'Bearer',
    'Bearer' : '442|UPWQqouwVCmFvNx5Z1jGZb4B2q4b9Vvo5q7UB0GI0d576b0f'
}

protected_resource_url = 'https://calendar.dev.thehead.ru/back-api/api/auth'


def get_token():
    response = requests.post(auth_url, data=login_data)
    if response.status_code != 200:
        raise Exception(f'Ошибка авторизации: {response.text}')
    return response.json()['access_token']


def test_protected_resource():
    token = get_token()

    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(protected_resource_url, headers=headers)

    assert response.status_code == 200, f'Ожидался код 200, но получен {response.status_code}'
    print("Доступ к защищённому ресурсу успешен!")


if __name__ == "__main__":
    test_protected_resource()