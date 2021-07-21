
test = [1, 2, 3, 4, 5]
print(test)
# Первый элемент в списке имеет index 0, второй элемент в списке имеет index 1, третий index 2 и т.д.
print(test[0])
print(test[1])
print(test[2])
print(test[3])
print(test[4])

# В списке можно хранить другие списки
test = [1, 2, 3, [4,5,6]]
print(test)
print(test[3][1])

test = ['a', 'b',['d','n','g'], 'c',]
print(test[2][2])


# списки также можно умножать
test = [1, 2, 3]
print(test * 3)

# В список можно добовлять с помощью плюса
test = [1, 2, 3]
print(test + [4, 5, 6])


# К строкам также можно обращатся как к списку
test = 'Привет'
print(test[2])

test = ['Alex Z', 'Open u', 'Zerr P0']
if 'Alex Z' in test:
    print("Alex Z is in list!")

test = [1, 3, 5, 6, 3, 8, 9]
if 4 in test:
    print("Found 4")
elif 8 in test:
    print("Found 8")
else:
    print("Not found 4")

test = [1, 2, 4, 5, 6]
if 3 not in test:
    print('3 not in list')

test = []
# добавление значений в список
# appennd добовляем значение в конец списка
#обьект.метод
test.append('Привет')
test.append(3)
test.append([1, 2, 3])
print(test)


# сколько элементов в списке
test = [5, 3, 2, 8, 7, 'testik']
#len(список)
print(f'В массиве test у нас находится {len(test)} элементов.')

# удаление из массива
#test.remove('8') хз раньше так тоже удаляло
test.remove(8)
test.remove('testik')
print(f'В массиве test у нас находится {len(test)} элементов.')

# Добовление элемента в список
test = [1, 2, 3, 4, 5, 6]
#  метод insert
# test.insert((куда, что))
test.insert(0, 7)
print(test)

# пример
nums = [1, 3, 4, 5, 8]
nums.append(4)
nums.insert(2,11)
print(len(nums))


test = [1, 2, 3, 5, 6, 6, 7, 6, 9]

# Функция max
# Самое большое значение
print(max(test))

# Функция min
# Самое меньшее значение
print(min(test))

# Подсчет количества повторяющихся элементов
print('Колчичество шестерок: ' + str(test.count(6)) + ' шт')


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Перевернуть список
test.reverse() # Этот метод преобразует списое (!!! Не возрощает, поэтому мы не можем сразу выполнить print(test.reverse()))
print(test)
