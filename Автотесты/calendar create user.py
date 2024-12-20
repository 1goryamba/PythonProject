import unittest
import requests

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://calendar.dev.thehead.ru/back-api/api'

    def test_post_user(self):
        new_user = {

            'first_name': 'Igor',
            'last_name' : 'Nikitin',
            'company_date':'2022-11-03',
            'vacation_days': '14',
            'email':'testingpython@gmail.ru',
            'phone':'79655352251'
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

    # def test_put_user(self):
    #     user_id = 1
    #     updated_user = {
    #         'name': 'Jane Smith',
    #         'email': 'janesmith@example.com'
    #     }
    #     response = requests.put(f'{self.base_url}/users/{user_id}', json=updated_user)
    #     self.assertEqual(response.status_code, 204)
    #     data = response.json()
    #     self.assertEqual(updated_user['name'], data['name'])
    #     self.assertEqual(updated_user['email'], data['email'])
    #
    # def test_delete_user(self):
    #     user_id = 1
    #     response = requests.delete(f'{self.base_url}/users/{user_id}')
    #     self.assertEqual(response.status_code, 204)
    #
    # def test_get_users(self):
    #     response = requests.get(f'{self.base_url}/profile')
    #     self.assertEqual(response.status_code, 200)
    #     data = response.json()
    #     self.assertIsInstance(data, list)
    #     self.assertGreater(len(data), 0)