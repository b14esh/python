#  Пример с git и JSON
import requests
import json
response = requests.get("https://api.github.com")
print(response.text)
data = response.json()

print(data)

print(data["current_user_url"])
print(data["current_user_authorizations_html_url"])
print(data["authorizations_url"])
print(data["code_search_url"])
