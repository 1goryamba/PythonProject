from faker import Faker
import requests

fake = Faker('ru_RU')

first_name = fake.first_name()
last_name = fake.last_name()
company_date = fake.date(pattern="%Y-%m-%d")
vacation_days = str(fake.random_int(min=1, max=30))
email = fake.free_email()
phone = fake.phone_number()
department_id = str(fake.random_int(min=1, max=2))

payload = {
    'first_name': first_name,
    'last_name': last_name,
    'company_date': company_date,
    'vacation_days': vacation_days,
    'email': email,
    'phone': phone,
    'department_id': department_id
}

url = "https://calendar.dev.thehead.ru/back-api/api/profile"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 409|K2BT5Qfu7IlMx7RBwiNJ2HXNthLH0m0n6xIRp0FT4cd7b7d9"
}
print(payload)

response = requests.post(url, data=payload, headers=headers)

print(f'Ошибка: {response.text}')

assert response.status_code == 201, f"Ответ {response.status_code}"
print(response.json())
print(payload)
