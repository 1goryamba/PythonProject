
import requests

url = "https://calendar.dev.thehead.ru/back-api/api/profile"
headers = {
    "Authorization": "Bearer 407|2lzpZcaszNdNovPtEW8FKEqNdwCWKSkuRtDXOvJ1613c0fb5"
}

response = requests.get(url, headers=headers)

assert response.status_code == 200, f"Ответ {response.status_code}"

print(response.json())