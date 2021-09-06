# Пример
# функция str() она возращает значение
# функция print() она не возращает, просто что то делает, в данном случае на экран выводит
converted = str(1232145)
print(converted)

# Создаем функцию каторая будет возращать значения
def max(x, y):
    if x > y:
        return x
    else:
        return y
print("TEST") # return остонавливает дальнейшие выполнение функции, поэтому эту строку мы никогда не увидим


# Проверяем нашу новую функцию max(x, y)
print(max(5, 9))
print(max(20, 10))

x = float(input('Число x: '))
y = float(input('Число y: '))
print(max(x, y))

# Переменные обьявленные внутри функции являются локальными для нее
# Тоесть мы не можем вызвать переменную из функции
#def test():
#    asd = 10
#test()
#print(asd) # вот тут ошибка.  мы не увидем значение переменной asd. Скрипт вылетит с ошибкой что переменная не назначенна





def print_X():
    print(1)
    print(2)
    return
    print(3)
    print(4)
print(print_X())





###!!! Внимание
# my_var = lol() # Вот так если записать то в переменную my_var вернется вывод функции lol()
my_var = lol  # А если записать так то мы сможим вызвать функцию вот так my_var()
my_var()



### Пример....
def shout(world):
    return world + "!"
speak = shout
output = speak('shout')
print(output)


### Еще пример
def lol2(name):
    """ Описание функции """
    print("LOL " + name + " !")
def read_me():
    return ':::' + input("Введите слово: ") + ':::'
lol2(read_me())


### Еще пример
def lol2(name):
    """ Описание функции """
    print("LOL " + name() + " !")
def read_me():
    return ':::' + input("Введите слово: ") + ':::'
lol2(read_me)