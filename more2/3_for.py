#Цыклы for
numbers = [1,2,3,4,5]
print(numbers)

print('\n')

for x in numbers:
    print(x)

print('\n')

for i in numbers:
    print(i)

print('\n')

for pohui in numbers:
    print(pohui)

print('\n')

for i in numbers:
    print(i*i)

print('\n')

numbers = range(1,6)
print(type(numbers))
for i in numbers:
    print(i)
print('\n')

for i in range(1,6):
    print(i)

print('\n')

for i in range(1,6):
    if i % 2 == 0:
        print(f'{i} is even') # четное
    else:
        print(f'{i} is odd') # не четное

print('\n')

numbers = [1,3,5,7,9]
for i, item in enumerate(numbers):
    numbers[i] *= 2
print(numbers)

print('\n')

name = "Jon"
for l in name:
    print(l)

print('\n')

for _ in range(5):  # Когда вводить именованнаую переменную нет смысла, можно использовать спец символ "_1"
    print('Alarm!')


typez = ('Jon', 'Ser', 22) # пройтись по картежу
for item in typez:
    print(item)

print('\n')

persons = [('WE',22), ('BOB', 23), ('SIR', 40)] # Пройти по списку содержащий кортежи
print(len(persons))
for (name,age) in persons:
    print(f'{name} is {age}')

print('\n')

players = dict(Char1=1111, Fox=2222, elfi=7855)
for item in players: # Для прохода по ключам
    print(item)

print('\n')

for v in players.values(): # для прохода по значениям ключей
    print(v)

print('\n')

for item in players.items(): # вот тут мы получим картежи...
    print(item)

print('\n')

for k,v in players.items(): # вот тут пройдем всетаки по ключам и значениям
    print(k,v)

print('\n')

# двойнной вложенный список
# двойной for
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
for x in list1:
    for y in list2:
        print(f" {x} + {y} = {x + y}")

print('\n')

list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]
pairs = []

for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x,y))
print(pairs)

