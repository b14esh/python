# формат для передачи данных
import json

class Tournament:
    def __init__(self, name, year):
        self.name = name
        self.year = year


tournaments = {
    "ALLOLO" : 2010,
    "ZAAAA" : 2015,
    "ZAZAZA" : 2019
}

# Метод json.dump - Позволяет сохронить в файл в формате JSON

# Метод json.dumps - возращает строку в виде JSON

json_date = json.dumps(tournaments, indent=2) # indent - стиль вывода - отступы # Сеарелизация # serialization
print(type(json_date))
print(json_date)

# json.load позволяет загрузить обратно из файла

# Метод json.loads позволяет преобразовать обратно из строки


loaded = json.loads(json_date) # Дисеарелизация # deserialization
print(type(loaded))
print(loaded)

t1 = Tournament("Aeroflot", 2010)
#json_data = json.dumps(t1) #!!!! Сложные обьекты нельзя  просто взять и сеарилезовать в JSON... в данном случае  классы

json_date = json.dumps(t1.__dict__)
print(json_date)
t = Tournament(**json.loads(json_date))
print(f'name={t.name}, year={t.year}')

