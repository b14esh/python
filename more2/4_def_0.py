# Встроенные функции
# математические функции
abs(-1)
abs(1)

max(1,2,3,4,5) # показать наибольшее число
min(1,2,3,4,5) # показать наименьшее число

max([1,2,3,4,5])
min([1,2,3,4,5])

pow(2, 8) # возведение в степень

round(3.37, 1) # округление числа

sum([1,2,3,4,5,6]) # сумма чисел # принемает список

#hex() # преобразует число в 10 формат / систему
#oct() # преобразует число в 8 формат / систему
#bin() # приобразует в двоичный формат / систему / бинарный формат

h = hex(42)
o = oct(42)
b = bin(42)
print(h, o, b)

# all возращает boolen, если все True вернет True, Если хотябы один False вернет False
all_true1 = all([True,True,True,True])
all_true2 = all([True,False,True,True])
print(all_true1, all_true2)

plr = [('x1', 2000), ('x2', 1900), ('x3', 1800), ('x4', 1700)]
z = all(rating > 1600 for _, rating in plr)  # правильный вариант, как только встретится False распечатает False
y = all([rating > 1600 for _, rating in plr]) # работает по другому, проходит по всем обьектам списка и только потом покажит результат
print(z)
print(y)

# any() если хотябы один элемент вернет True аспечатает True
# any() работает со списком
any_true1 = any([True,True,True])
any_true2 = any([False,False,False])
any_true3 = any([False,True,False])
print(any_true1, any_true2, any_true3)
plr = [('x1', 2000), ('x2', 1900), ('x3', 1800), ('x4', 1700)]
z = any(rating < 1750 for _, rating in plr)
print(z)

# zip()   Склейка обьектов
# При склейки лишнии элементы будут отсечены
letters = 'abcd'
numbers = (1, 2, 3, 4, 5)
zipped = zip(letters,numbers)
print(type(zipped))
print(zipped)
zipped_list = list(zipped)
print(zipped_list)

# zip()
name = ['na1', 'na2', 'za', 'go']
rating = [1000, 700, 900, 350]
players = dict(zip(name, rating))
print(players)


# input() ввод от пользователя
# replay = input()
# print(replay)

# юникод # преобразование
# символьные таблицы
code = ord('a')
c = chr(code)
print(code, c)

