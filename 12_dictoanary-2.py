#   (----item------)
#   (key)    (value)
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'awards': ['nagrada1', 'nagrada2'],
    'image': ['image1.jpg','image2.jpg','image3.jpg'],
}
print(enemy)
print(enemy['loc_x'])
pp = "-----------------------------------------------"
#массивы
all_enemies = []
#all_enemies.append(enemy)
#all_enemies.append(enemy)
#all_enemies.append(enemy)
#print(all_enemies)
for x in range(0,10):
#    all_enemies.append(enemy) ошибка выполняется клонирование. и если в дольнейшем использовать это то будут проблемы
    all_enemies.append(enemy.copy())
print(all_enemies)
print(pp)
for x2 in all_enemies:
    print(x2)
print(pp)
all_enemies[5]['health'] = 30
all_enemies[1]['name'] = 'Vasya'
all_enemies[3]['name'] = 'Petre'
all_enemies[6]['name'] = 'Ot'
all_enemies[8]['name'] = 'Kozel'
#all_enemies[2]['loc_x'] = all_enemies[2]['loc_x'] + 10
all_enemies[2]['loc_x'] += 10
for x2 in all_enemies:
    print(x2)
print(pp)
print(all_enemies[5])
print(pp)