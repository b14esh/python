# tuple похож по работе на список
# tuple \ картеж \ не именяемый списк
# точнее не возможно изменить одно значение
# катеж можно изменить целиком
string = ('str1', 'str2', 'str3')
# string[0] = 'xxx' # при попытке изменить первое значение получим ошибку
# TypeError: 'tuple' object does not support item assignment
print(type(string))

person = ('x1', 'x2', 22)
print(type(person))


print(person[0])
print(string[2])


# Изменение картежа целиком
string = ('str1x', 'str2', 'str3')
person = ('z1', 'x2', '22', 'z1', 'z1')

# Показать элемент по индексу
print(person[0])
print(string[0])

# Показать количество симваолов
print(len(person))
print(len(string))


# Посчитать количество уникальных элеменов
print(person.count('z1'))
print(string.count('str2'))

# Показать индекс элемента по ключу
print(person.index('22'))



# namedtuple
# Позволяет проименовать
#players = [('z1',100,222 ), ('z2', 1000 , 2) , ('z3', 500, 300)]
from collections import namedtuple
#Player = namedtuple(('Player', 'name num1 num2')
#players = [Player('z1', 100, 222 ), Player('z2', 1000 , 2), Player('z3', 500, 300)]
#print(players[0])

#p1 = Player('a1', 123, 233)
#print(p1.a1)
#print(p1.num1)
#print(p2.num2)

