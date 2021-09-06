#  Пример с git и JSON
import requests
import json
response = requests.get("https://api.github.com")
#print(response.text)
data = response.json()

#print(data)

# Выведим заголовки
blog_response = requests.get("https://b14esh.com")
git_response = requests.get("https://api.github.com")

print(blog_response.headers, end='\n') # выведим заголовки
print('')
print(git_response.headers, end='\n') # выведим заголовки

print("\n")
print(blog_response.headers["content-type"]) # можем обратится вот так
print(git_response.headers["content-type"])  # можем обратится вот так

print("\n")
placeholder_response = requests.get("https://jsonplaceholder.typicode.com/comments", params=b'postId=1')
#print(placeholder_response.text)
print(placeholder_response.json())