import requests

url = 'https://calendar.dev.thehead.ru/back-api/api/auth/me'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 409|K2BT5Qfu7IlMx7RBwiNJ2HXNthLH0m0n6xIRp0FT4cd7b7d9'
}

payload = {
    "email": "test2@example.com",
    "password": "password"
}

response = requests.get(url, headers=headers, json=payload)

print(f"Ответ сервера:\n{response.text}")

if response.status_code == 200:
    print("\nУспех!")
else:
    print(f"\nОшибка! Статус-код: {response.status_code}")