# форматирование строк
#Привет, ИМЯ!
#Тебе уже ЛЕТ!
name = "Вася"
age = 36

z = "Хрюндель"
x = 77

print("контентенация:")
print("Привет, " + name + "." + "\nТебе уже "+ str(age) + " лет.")

# % - placeholder
# %s - placeholder string - строки
# %d - placeholder digit - числа
# %f - placeholder float - дроби
print("\nФорматированые строки в стиле printf:")
print('Привет, %s!\nТебе уже %d лет!' %(name, age))



# .format()
print("\nФорматированые строки вариант номер раз:")
print("Привет, {}. \nТебе уже {} лет." .format(name, age))
print('{0}{1}{0}'.format('abra', 'cad'))
print('>>> {0} , {1} , {0} <<<<'.format('abra', 'cad'))
print("Привет, {name}. \nТебе уже {age} лет." .format(name = z, age = x))

print("\n")
human  = {
    "name" : "Voodoo",
    'age'  : 21
}

print( "Имя: {name}. \nВозраст: {age}" .format( name = human['name'], age = human['age']))
print( "Имя: {person[name]}. \nВозраст: {person[age]}" .format( person = human))




human = {
    'name' : 'Jessy',
    'age' : 21
}

print('\n')
#****Jessy****
#____Jessy____
#___Jonatan___
#ASDSDSASASASA
#AAAWWEFFFSSS_
# Методы заполнения
# первый метод заполнения Jessy***** ставим знак <
# второй метод заполнения *****jessy ставим знак >
# третий метод заполнения **Jessy*** ставим знак ^
#print('Hello {0:ЗнакзаполненияМетодКол-во}'.format(input_str))
input_str = "jessy"
print('Hello {0:*<20}'.format(input_str))
print('Hello {0:*>20}'.format(input_str))
print('Hello {0:*^20}'.format(input_str))


# Пример авто выравинвания
print('\nБыло вот так-вот: {0:*^10}'.format(input_str))
print(f"Длина строки слова: {len(input_str)} ")
print(f"Результат деления по модулю: {(len(input_str)%2)}")
length = 10
if(len(input_str)%2):
    length += 1
print(f"Прибавили один, стало {length}.")
print(('Получили красиво и ровно: {0:*^'+str(length)+'}').format(input_str))



print("\nФорматированые строки вариант номер два:")
print(f"Привет, {name}.\nТебе уже {age} лет.")



