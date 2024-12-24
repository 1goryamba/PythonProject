import requests

url = 'https://calendar.dev.thehead.ru/back-api/api/profile'
token = '402|vbuNda3hvmlLv8kJ5CMVTDIwIzGl6we8mYwaSJcCdcd34626'
headers = {
    'Authorization': f'Bearer {token}'
}

payload = {
    'first_name': 'Testing',
    'last_name': 'Testing',
    'company_date': '2022-11-03',
    'vacation_days': '1',
    'email': 'test@testhead.ru',
    'phone': '79655352252',
    'department_id': '1'
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200 or response.status_code == 201:
    print("Профиль успешно создан!")
else:
    print(f"Произошла ошибка: {response.status_code}")