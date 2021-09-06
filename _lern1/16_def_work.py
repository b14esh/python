# Функции для работы со строками и числами
fruits = ['Лимоны', 'Яблоки', 'Киви', 'Ананас', 'Клубника']
members = 'James,Jonny,Jessie,Jack,John'

# join, replace, startswitch, endswith, lower, upper, split, min, max , abs, sum


# Пример statswitch
name = "Алешка"
#name = input('Ваше имя: ')
# Если имя начинается с , большой буквы А
if (name.startswith('А')):
    print("Добро пожаловать!\nВаше имя начинается на букву А")
else:
    print("Добро пожаловать")


# Пример endswith
word = 'Hello drudving'
if(word.endswith('ing')):
    print('Hello ING')
else:
    print('Hello!!!')

word = 'Hello Dredd'
if(word.endswith('ing')):
    print('Hello ING')
else:
    print('Hello!!!')





#Пример lower
if (name.lower().startswith('А') or name.lower().startswith('A')):
    print("Добро пожаловать!\nВаше имя начинается на букву А")
else:
    print("Добро пожаловать")

x = "ПрРиВеТ ДруГ VaSya"
print(x.lower())

# Пример upper
x = "ПрРиВеТ ДруГ VaSya"
print(x.upper())




#print(fruits)
#i = 0
#for fru in fruits:
#    print(fruits[i])
#    i +=1


#print(members)
#i = 0
#for xxx in members:
#    print(members[i])
#    i += 1
#    if i == 5:
#        break


# Split (обратное действие join) разбивает строку на список....
print(members)
print(members.split(','))

# MIN определяет из списка самы минемальный элемент
print(min(1,2,56,234,235,99,84345,23))

# MAX определяет из списка самый высокий элемент
print(max(1,2,56,234,235,99,84345,23))


# abs()
# abs - абсолютное число
# абсолютное число это число у которого отсуствуют какие либо знаки
print(abs(1000))
print(abs(-1000))

#sum
# сумирование списков
print(sum([50,250,234,3242]))
