# Может сожержать уникальные элементы
# Во множестве не будет дубликатов

my_set = set()
print(my_set)
print(type(my_set))

my_set.add(1) # добавим значение во множестов
print(my_set)
my_set.add(2)

print(my_set)
my_set.add(2)

print(my_set)

my_list = [1,2,2,2,2,2,2,3,4,5,1,1,1,1,4,4,4,4,4,4,5] # создали список
print(my_list)

s = set(my_list) # Добавим  лист в множество
print(s)

print(len(s))

print(1 in s)
print(5 in s)
print(6 in s)


set1 = {1,2,3,4}
set2 = {1,2,3,4,5}

# is sub set
# Сравнение множеств
print(set1.issubset(set2))
print(set2.issubset(set1))

print(set2.issuperset(set1))

#
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2))

# обьединение
set1 = {1,2,3,4}
set2 = {1,2,3,4,5}
set3 = set1.union(set2)
print(set3)

# пересечение
set3 = set1.intersection(set2)
print(set3)

# дифиренс diff
set1 = {0,1,2,3,4}
set2 = {1,2,3,4,5}
set3 = set1.difference(set2)
set4 = set1.symmetric_difference(set2)
print(f"\n{set3}\n{set4}")

# update
set1.update(set2)
print(set1)

# удаление
set1.remove(1)
print(set1)
#set1.remove(42) # Будет ошибка KeyError
set1.remove(2)
print(set1)
set1.discard(2)
set1.discard(42) # ошибки не будет
print(set1)

popped_out_element = set1.pop() # pop удаляет один случайный элемент и возращает инф что удалил
print(popped_out_element)

# Очистка множества
set1.clear()
print(set1)


