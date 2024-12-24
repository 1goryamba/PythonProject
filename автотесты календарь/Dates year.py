import requests

url = "https://calendar.dev.thehead.ru/back-api/api/dates/year/2024"
headers = {
    "Authorization": "Bearer yFGfpeL0f1vrUW52wcRjzzPjs0wfP6I3P4hhPB4Caae356c8"
}

response = requests.get(url, headers=headers)

assert response.status_code == 200, f"Ответ {response.status_code}"

print(response.json())