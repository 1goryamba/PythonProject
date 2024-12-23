import requests
import pytest
import unittest

# Авторизация

@pytest.fixture(scope="module")
def get_auth_token():
    url = "https://calendar.dev.thehead.ru/back-api/api/auth"
    payload = {"email": "test2@example.com", "password": "password"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception("Authentication failed!")

    return response.json()


def test_authentication(get_auth_token):
    assert get_auth_token.get("status") == 200
    assert "token" in get_auth_token["data"].keys()
    assert len(get_auth_token["data"]["token"]) > 10

# Создание пользователя

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://calendar.dev.thehead.ru/back-api/api'

    def test_post_user(self):
        new_user = {

            'first_name': 'Testing',
            'last_name' : 'Testing',
            'company_date':'2022-11-03',
            'vacation_days': '14',
            'email':'test@test.com',
            'phone':'79999772277'
        }
        response = requests.post(f'{self.base_url}/profile', json=new_user)
        self.assertEqual(response.status_code, 204)
        data = response.json()
        self.assertIn('id', data)
        self.assertEqual(new_user['avatar'], data['avatar'])
        self.assertEqual(new_user['first_name'], data['first_name'])
        self.assertEqual(new_user['last_name'], data['last_name'])
        self.assertEqual(new_user['company_date'], data['company_date'])
        self.assertEqual(new_user['vacation_days'], data ['vacation_days'])

    if __name__ == '__main__':
        unittest.main()