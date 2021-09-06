# словари
d = {}
print(d)

# наполнение

d = {'test' : 1, 'test2': "TeSt"}
print(d['test'])
print(d['test2'])
print(d)

# dict

d = dict(short='dict', longer='dictonary')
print(d)
d['short'] = 234

print(d)

# dict
d = dict([(23, 34), (56, 87)])
print(d)

# dict
d = dict.fromkeys(['a', 'b'])
print(d)

d = dict.fromkeys(['a', 'b'], 1)
print(d)

d = dict.fromkeys(['a', 'b','c'], 1)
print(d)


# dict
# ** возведение в степень
d = {a: a ** 2 for a in range(7)}
print(d)
d = {a: a * 1 for a in range(7)}
print(d)
d = {a: a + 1 - 1 for a in range(7)}
print(d)

# dict +  list
# тут у нас словарь person, в него вложенны словари name, address, phone
# в значени словоря 'address' вложен список
# в значения ключей name и phone вложенны словари
person = { 'name' : {'last_name': 'Иванов', 'firts_name': 'Иван','middle_name': 'Иванович'}, 'address': ['г.Хм','ул. Налка, д. 23', 'кв.12'], 'phone': {'home_phone': '11-22-33', 'mobile_phone': '8-45-324-245-4','mobile_phone2': 'Нет'}}
print(person['name'])
print(person['name']['firts_name'])
print(person['name']['last_name'])
print(person['address'][1]) # обрати внимане тут сначала словарь а в словарь вложен список
print(person['phone']['mobile_phone'])


# методы словарей
# dict.clear() - очищает словарь
# dict.copy()  - возрощает копию словаря
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value( по умолчанию None)
# dict.get(key,default) - возрощает значение ключа, но если его нет, не бросает исключение, а возврощает default(по умолчанию None)
# dict.items() - возращает пары (ключ,значение)
# dict.keys() - возращает ключи в словаре
# dict.values() - возрощает значения в словаре
# dict.pop(key[, default] - удаляет ключ и возрощает значение. Если ключа нет то возрощает default(по умолчанию бросает исключение)
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

d = {'test' : 1, 'test2': "TeSt"}
z = d.items()
x = d.keys()
y = d.values()

print('\n', z,'\n', x, '\n', y)

print('\n')

print(person.keys())
print('\n')

print(person.values())
print('\n')

person.clear()
print(person)
