int_list = [1,2,3]
mix_list = [2.0, 1 , "string"]
print(len(int_list))
print(len(mix_list))
print(int_list[0])
print(mix_list[-1])
print(int_list[1:]) # срезы


# Обьеденение списков
name1 = ['aaa', 'bbb', 'cccc']
name2 = ['zxc', 'xxx']
names = name1 + name2
print(names)

# Обьеденение списков
mix_all =  int_list + mix_list + names
print(mix_all)

# Изменить значение в списке
name1[0] = ['123']
name1[2] = ['223']
print(name1)

# Добавить в список
names.append('XXX123')
names.append('x2434')
names.append('xda')
print(names)


# Удалить последнее значение в списке и вывести что мы удалили
poped = mix_all.pop()
print(poped)

# Удалить элемент например значение 5 и вывести что мы удалили
poped = mix_all.pop(5)
print(poped)

# Сортировка списка
abzac = ['aaa', 'bbb', 'cccc', 'zxc', 'xxx']
nomer = [1, 4, 6, 3, 4, 6, 0, 000]
letters = ["ac", "ab", "aa"]
letters1 = ["abc", "a", "ab"]
abzac.sort()
nomer.sort()
letters.sort()
letters1.sort(key=len) # сортировка по количеству символов
print(f"{abzac} \n{nomer} \n{letters} \n{letters1}")

# Переворачивоние списка
nomer = [1, 4, 6, 3, 4, 6, 0, 000]
nomer.reverse()
print(nomer)

# Сортировка по убыванию
nomer = [40, 234, 231, 22, 555, 777, 123,13,13,13]
print(nomer)
nomer.sort(reverse=True)
print(nomer)

# Вставка обьекта
nomer.insert(1, 100)
nomer.insert(7, 33)
nomer.insert(-2, 43)
print(nomer)

# Поиск обьекта
print(nomer.index(555)) # Поиск индекса по имени обьекта
so = nomer.index(231)
print(f"В списке \"nomer\" у числа \"231\" индекс равен {so}")

# Посчитать количество определенного обьекта в списке
print(f"В списке \"nomer\" число \"13\" повторяется {nomer.count(13)} раза.") # Распечатает кол-во повторений числа 13 в списке

# Копирование списка
zomer = nomer.copy()
print(zomer)

# Очистка списка
nomer.clear()
print(nomer)

