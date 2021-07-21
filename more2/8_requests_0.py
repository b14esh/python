# Для работы с http \ https

import requests

# Запрос функция GET
response = requests.get("https://b14esh.com")
print(response)
print(type(response))
print(response.status_code)

if response:
    print("Works!")
