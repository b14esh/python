# списки
pp = "\n#---------------------------------------------------------\n"

print(pp)

l = []
lis = [1, 56, 'x', 34, 2.34, ['S','t','r','o','k','a']]
print(lis)
print(pp)

a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)

print(pp)
l.append(23)  # append добавить в конец списка
l.append(34)
print(l)

print(pp)
b = [24, 67]
l.extend(b)   # расширить список другим списком
print(l)

print(pp)
l.insert(1, 56) # вставить по индексу 1 значение 56
print(l)

print(pp)
l.append(34)
l.remove(34) # удалится первый элемент со значением 34
print(l)

print(pp)

l.pop()  # принемает индекс элемента и удаляет его, если не указывать удалится последний элемент в списке
print(l)
print(pp)
l.pop(0)  # индекс элемента указан он будет удален в нашем случае это число 23
print(l)
print(pp)

print(l.index(56)) # l.index возращает индекс элемента

print(pp)

print(l.count(24)) # l.count возращает количество элементов со значение 24

print(pp)

#l.sort() # сортерует список
#l.remove() # переворачивает список
#.clear() # очищает список

a = [1,3,4,5,6,7,24,525,12,45,6]
x = [99,666,777]
a.extend(x)
print(a)

print(len(a))  # показывает количестов элеметов в списке

print(pp)

z = ['r','e','s','e','t']
print(z)
z.extend(x)
print(z)
z.pop(1)
z.pop(-2)
print(z)
