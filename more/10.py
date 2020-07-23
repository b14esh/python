# картежи похожи на списки
# отличие, изменять одно значение индекса нельзя
# картежи занимают меньше места в памяти
#a = (43, 56, 45.23, 'd') #картеж
#b = [43, 56, 45.23, 'd'] #список

#a[0] = 34 # Картежи изменить так нельзя будет ошибка, изменить можно только целиком
#b[0] = 44 # а вот со списком будет все хорошо
#print(a.__sizeof__())
#print(b.__sizeof__())

#a = tuple ("hello world")
#print(a)

#a = "hello world", "sdf", 345 # картеж , запетая решает что это картеж.....

a = ("hello world", "sdf", 345) # правильная запись картежа
print(a)
print(a.count(345))
print(a[1])
