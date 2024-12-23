import requests

url = 'https://calendar.dev.thehead.ru/back-api/api/auth'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 409|K2BT5Qfu7IlMx7RBwiNJ2HXNthLH0m0n6xIRp0FT4cd7b7d9'
}
data = {
    'email': 'test2@example.com',
    'password': 'password'
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Успешная авторизация!")
else:
    print(f"Произошла ошибка: {response.status_code}")