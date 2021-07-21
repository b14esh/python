# формат для передачи данных
# https://jsonplaceholder.typicode.com/ - сайт для поигратся с json
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
print(type(json_data))
print(json_data)

decode_players = ChessPlayer.from_json(json.loads(json_data))
print(decode_players)
print(decode_players.tournaments)

with open("player.json", "w") as file:
    json.dump(p1, file, default=lambda obj: obj.__dict__)

with open("player.json", "r") as read_file:
    data = json.load(read_file)

print(data)

decode_players = ChessPlayer.from_json(data)
print(decode_players)
print(decode_players.tournaments)


# Пример выгрузки
#import  requests
#response = requests.get(https://jsonplaceholder.typicode.com/todos)
#todos = json.loads(response.text)
#todos