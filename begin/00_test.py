# комент
a = 500
b = 700
z = a + b
print(z)
# при print печатаются всегда буковки, если нам нужно печатать буквы и цифры вместе необходимо
# для циферок указывать параметр str
print("Зед равно: " + str(z))
print(a +  b + z - a + 100 - 200 + 4 - 25)
print("А=" + str(a) + "," + " B=" + str(b) +"," + " A+B=" + str(z) )
print(f"А = {a}, B = {b}, A + B = {z} ")

f_name = "Vasia"
l_name = "Zaez"
age = 100
full_name = (f_name + " " + l_name)
full_name_z = (f"Челобрека зовут: {f_name} {l_name}, и живет он уже: {age} лет")
print(full_name)
print(full_name_z)

# 1
x = "\n----------------------------\n"
print(x)
# Заглавные буковки
# Редактирование текста
name = "mr VaSia pUpkIn"
print(name)
print(name.title())
print(name.upper())
print(name.lower())

print("Privet stroka nomer 1\nPrivet stroka nomer 2\nPrivet stroka 3 ")
print(x)
print("Message:\n\t Message1\n\t Message2\n\t Message3 \nEND")
print(x)
print("Lower name: " + name.lower())
print("Upper name: " + name.upper())
print("Title name: " + name.title())
print(x)
# Подрезаем лишнее
a = "      . , dadya vasya .      "
print(a)
print(a.strip())
print(a.lstrip())
print(a.strip())
a = "....., dadya vasya ,....."
print(a.strip("."))
b = a.strip(".")
c = b.strip(",")
e = c.strip()
print(e)
print(x)
a = "....., dadya vasya ,....."
print(a.strip("."))
a = a.strip(".")
a = b.strip(",")
a = c.strip()
print(a)
print(x)

#### Циферки
num1 = 30
num2 = 45
num3 = num1 + 10
print(num1 + num2)
print(num3)

print(x)

x1 = 55555555555555555555555555555555555555555555555555555555555555555555555555555
x2 = 88888888888888888888888888888888888888888888888888888888888888888888888888888
print(x1 + x2)
print(x1*x2 + 10)
print(num2/3)

print(x)

x1 = 6
x2 = 4
print(x1 / x2)

print(x)

print((10*2)/(5+100))
print(x)

# Дщщпы ...... Loops for
print("бесконечно печатать могу копипасть ")
pp = "\n----------------------------\n"
print(pp)
for x in (range(0,5)):
    print("бесконечно печатать ")
print(pp)
for x in range(0,5 + 1):
     print(x)
print(pp)
for x in reversed(range(0,5)):
    print("бесконечно печатать Да да ")
    print(f"нет кончусь {x}")
print(pp)
for x in range(2,12,2):
    print(x)
print(pp)
for x in range(-10,12,5):
    print(x)
print(pp)
for x in range(-10,12,5):
    print(f"x = {x}")
    if x == 5:
        break
print(f"Все приехали x = {x}")
print(pp)
x = 0
while True:
    print(x)
    x = x+ 1
    if x == 5:
        break
print(pp)
x = 0
while True:
    print("LOL")
    print(x)
    print("no")
    x = x + 1
    if x == 3:
        break
print(pp)
while True:
    print(f"XO XO XO find x now = {x}")
    x = x+1
    if x == 10:
        break
print(f"End x = {10}")
print(pp)

### МАССИВЫ ARRY LIST

cities = ['New York', 'Moscow', 'new dehli', 'Simper', 'Torr']
print(cities)
print(cities[0])
print(len(cities))
print(cities[4])
print(cities[2])
print(f"Третий город в массиве {cities[2]}")
print(f"Последний город в массиве {cities[-1]}")
print(f"Первый город в массиве {cities[0]}")
print(pp)
y = cities[2]
y = y.title()
print(f"Напечатаем та как нибуть красиво третий город << {y} >> ")
print(pp)
print(f"А теперь включим мозг и распечатаем красивше << {cities[2].upper()} >>")
print(pp)
print(f"Выведим содержимое массива cities: \n\t было: {cities}")
cities[2] = 'Tula'
print(f"\tстало: {cities}")
print(f"Мы видим что третий город изменился на {cities[2]} ")
print(pp)
cities.append('Kurks')
print(f"Список был такой: \n\t {cities} \nДобавили новый город в конец списка: \n\t {cities[-1]} \n\tСписок стал такой: \n\t {cities}")
cities.append('Yalta')
print(f"Добавили еще один город: \n\t {cities[-1]} \nСпиcок стал таким: \n\t{cities}")
cities.insert(2,'Feodosia')
print(f"Добавили новый город {cities[2]} в список после третьего города. \nСписок стал таким: \n\t{cities}")
print(pp)
print(f"Показать трейтий город с конца: \nЭто у нас: \n\t >>> {cities[-3]} <<<")
del cities[-3]
print(f"Удалили третий город, хочу посмотреть список: \n\t {cities}")
cities.remove('Feodosia')
print(f"Научились удалять по названию и удалили город Feodosia. \nТеперь список вот такой: \n\t {cities}")
print("Городов у нас в списке всего то: " + str(len(cities)))
deleted_city = cities.pop()
print("Научились еще одному удалению и удалили последний город из списка: " + deleted_city)
print("Городов у нас в списке всего то: " + str(len(cities)))
print(pp)
cities.sort()
print(f"Научили нас сортировки массива. Печатаем что мы там отсортировали: \n\t {cities}")
print(pp)
cities.sort(reverse=True)
print(f"Научили нас сортировать в обратном порядке. \n Печатаем: \n\t {cities}")
print(pp)
cities.reverse()
print(f"Научили нас просто переворачивать список без сортировки(правдо отсортерован он уже командами выше): \nПечатаем: \n\t {cities}")
print(pp)