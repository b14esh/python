# Словари
# если в значении цифры то записать можно так
players = dict(one=2800, two=2700, JOJ=1000)


# Но правильная запись будет такая

players = {
    "one" : "2800",
    "two" : "2700",
    "JOJ" : "1000",
    "MOB" : "RO",}

top1 = players['one']
top2 = players["two"]
top3 = players["JOJ"]
top4 = players["MOB"]

print(f"На первом месте у нас {players['one']} \nНа втором месте у нас {players['two']} \nНа третьем месте у нас {players['JOJ']} \nНа последнем месте у нас {players['MOB']} ")

# Пожно получить значение ключа используя get
print("\n" + players.get('one'))

# Изменить значение
players['MOB'] = '1000'
print(f"\nНа первом месте у нас {players['one']} \nНа втором месте у нас {players['two']} \nНа третьем месте у нас {players['JOJ']} \nНа последнем месте у нас {players['MOB']} ")

# Добавить нового
players['So'] = '1500'
print(f"\nНа первом месте у нас {players['one']} \nНа втором месте у нас {players['two']} \nНа третьем месте у нас {players['JOJ']} \nНа последнем месте у нас {players['MOB']} \nНа последнем месте у нас {players['So']}")

# Удаление
del players['So']
print(f"\n{players} ")

# Просмотр ключей словаря
keys = players.keys()
print("\n")
print(type(keys))
print(keys)

# Иногда удобнее получить список ключей
l = list(players.keys())
print(type(l))
print(l)

# А можно сразу получить отсортерованный список ключей с помощью sorted
print(sorted(players.keys()))

# Проверка если в славоре ключ one
print('one' in players)

# Проверить нет ли в словоре ключа ZOBGTA
print('ZOBGTA' not in players)

# Показать все значения списка
vals = players.values()
print(type(vals))
print(vals)

# Иногда удобнее получить список значений
vals_list = list(players.values())
print(type(vals_list))
print(vals_list)

# сортировка / получить отсортерованный список значений ключей
print(sorted(players.values()))

# копия
players_copy = players.copy()

print(players_copy)

# очистка
players.clear()
players_copy.clear()
print(players)
print(players_copy)

#Вывод ключа и значения функция items()
for k,v in players_copy.items():
    print(f" чувак {k} очков {v}")
print("\n")
test = {
    "ключ1" : "значение1",
    "ключ2" : "значение2",
    "ключ3" : "значение3",
    "ключ4" : "значение4",
    "ключ5" : (1,2,3,4,5,6,7),
    "ключ6" : {"что": "оО", "Бу":"Нет1"},
    "zzzz" : False,
    "xxxx" : True,
     125 : "Сто двадцать пять"

}
print("\n")
for k,v in test.items():
    print(f" {k} {v}")

contacts = {
    "Лось": "1234567",
    "Лис":"5555555",
    "Зубра":"999"

}

print("\n")
for nasrt1,nasrt2 in contacts.items():
    print(f" {nasrt1}  {nasrt2}")

# Удаление
print("\n")
players = {
    "one" : "2800",
    "two" : "2700",
    "JOJ" : "1000",
    "MOB" : "RO",}

players.pop('MOB')
print(players)

# Удаление с конца
print(players.popitem()) # также функция popitem озрощает то что она удалила
print(players)

# Посчитать количество ключей+значение
print(len(players))

# Добовляет ключ со знпчением None
players.setdefault('Xdsdsdsdsf')
print(players)