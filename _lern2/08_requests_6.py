#  Пример с git и JSON
import requests
import json
# формат для передачи данных
import json

class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def from_json(cls, json_date):
        return  cls(**json_date)

class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

    @classmethod
    def from_json(cls, json_data):
        tournament = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournament)

t1 = Tournament("Aer 19", 2019)
t2 = Tournament("Aer 17", 2017)
t3 = Tournament("Aer 15", 2015)
t4 = Tournament("Aer 12", 2012)

p1 = ChessPlayer([t1, t2, t3, t4])

json_data = json.dumps(p1, default=lambda obj: obj.__dict__, indent=4, sort_keys=True)

response = requests.post("https://httpbin.org/post", json=json_data)
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])

from getpass import getpass
#auth_response = requests.get("https://site.com", auth=('user_name', 'user_passwords'))
#auth_response = requests.get("https://api.github.com/user", auth=("usename", getpass()))

#auth_response_call = auth_response.json()
#auth_response_call = auth_response.text

#print(auth_response_call)