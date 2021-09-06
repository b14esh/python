pp = "--------------------------------------------"
#         0      1     2         3      4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada' ]
for x in cars:
    print(x)
print(pp)
for x in cars:
    print(x.upper())
print(pp)
for x in cars:
    print(x.title())
print(pp)
for x in cars:
    print(x.lower())
print(pp)
mynumber_list = list(range(0,10))
print(f"Тут нас научили создовать список с циферами. \n Вот и он: \n\t {mynumber_list}")
print(f"А теперь мы его выведем и выполним умножение на 2 :")
for x in mynumber_list:
    x = x*2
    print(x)
print(pp)
mynumber_list.sort(reverse=True)
print(f"Напечатаем отсортированый список с цифрами в обратном порядке: \n\t {mynumber_list}")
print(pp)
print(f" научили показать максемальную цифру из списка: >>> {max(mynumber_list)} <<<")
print(f" научили показать минемальную цифру из списка: >>> {min(mynumber_list)} <<<")
print(f" научили показать сумму цифр из это-го списка: >>> {sum(mynumber_list)} <<<")
print(pp)
# [начать_с_1 : и_до_какого выбрать_4 ]
mycars = cars[1:4]
print(f"Покажит три машины из списка mycars. \n\t {mycars}")
print(pp)
mycars = cars[:]
print(f"Покажит от начала списка и до конца \n\t {mycars}")
mycars = cars[:2]
print(f"Покажит от начала списка и до 3(без 3)  \n\t {mycars}")
mycars = cars[-3:]
print(f"Покажит от третьго с конца и до конца \n\t {mycars}")
mycars = cars[-3:-2]
print(f"Покажит от третьго с конца и до второго с  конца \n\t {mycars}")
mycars = cars[:] #копия массива
print(pp)
print(mycars)
print(pp)

x = 25
if x == 25:
    print("YES x == 25")
else:
    print("NO x != 25")
print(pp)
age = 3
if age <= 4:
    print(f"small age {age}")
elif age > 4 and age < 12:
    print(f"medium age {age}")
elif age >= 12 and age <19:
    print(f"normal age {age}")
else:
    print(f"old age =  {age}")
print(pp)
all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print("YES LADA +++")
else:
    print("NO LADA")
print(pp)

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " German cars")
    else:
        print(xxxx + "is not german cars")
print(pp)
for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " German cars")
print(pp)
### Словари
#       {-----Item------}
#         {key} : {value}
enemy = {
         'loc_x':  70,
         'loc_y':  50,
         'color': 'green',
         'health': 100,
         'name': 'General',
}
print(enemy)
print(pp)
print(f"Location X = {enemy['loc_x']}")
print(f"Location Y = {enemy['loc_y']}")
print(f"Name = {enemy['name']}")
print(pp)
enemy['rank'] = 'General'
print(enemy)
print(pp)
del enemy['rank']
print(enemy)
print(pp)
enemy['loc_x'] = enemy['loc_x'] +40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'
print(enemy)
print(pp)

print(enemy.keys())
print(enemy.values())
print(pp)

