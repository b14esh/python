import requests
response = requests.get("https://b14esh.com")

print(response.content) # показать содержимое страницы  # выведит в одну строку

response.encoding = 'utf-8' # задать кодировку
print(response.text)  # показать содержимое страницы
