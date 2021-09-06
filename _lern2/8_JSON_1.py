# формат для передачи данных
import json

class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


class ChessPlayer:
    def __init__(self, tournaments):
        self.tournaments = tournaments

t1 = Tournament("Aer 19", 2019)
t2 = Tournament("Aer 17", 2017)
t3 = Tournament("Aer 15", 2015)
t4 = Tournament("Aer 12", 2012)

p1 = ChessPlayer([t1, t2, t3, t4])

#json_date = json.dumps(p1.__dict__) #!!!! Сложные обьекты нельзя  просто взять и сеарилезовать в JSON... в данном случае  классы
json_date = json.dumps(p1, default=lambda obj: obj.__dict__)
print(json_date)

decoded_player = ChessPlayer(**json.loads(json_date)) # пробуем выгрузить
print(decoded_player) # вроде все ок НО....

player_tournaments = decoded_player.tournaments[0]
print(type(player_tournaments))
print(player_tournaments)