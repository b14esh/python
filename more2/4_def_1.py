# Функции нужны для того что бы не повторять один и тот же код несколько раз
# переиспользование кода
# упращение кода
# чистый код
# меньше ошибок


# def define определить
# Пример
def greeting():
    '''
    DOC STRING:  FOR HELP
    INPUT: NOFING
    OUTPUT: HELLO
    '''

    print('Hello')

greeting()


# Поссмотреть помощь по функции
help(greeting)

# Еще пример
def print_name(name):
    print(name)

print_name('Alex')


# еще пример с переменной по умолчанию
def print_name1(name='ENTER_NAME'):
    print(name)
print_name1()
print_name1('Vasya')


# возрощаемый тип функций
result = print_name1()
print(result)
print(type(result))


# пример возращающей функции
def get_greeting(name):
    return 'Hello ' + name

greeting = get_greeting('Ell')

print(greeting)


# пример возращающей функции
def get_sum(a,b):
    return a+b

result = get_sum(10,15)
print(result)


# # пример возращающей функции
def is_adult(age):
    return age >= 18

is_adult = is_adult(21)
print(is_adult)


# пример возращающей функции
# палиндром это когда строка одинаково читается с начало и с конца
def is_palindrome(text):
    return  text == text[::-1]

print(is_palindrome('aabaa'))
print(is_palindrome('aabba'))

# пример возращающей функции
def calc_texes(p1,p2,p3):
    return sum((p1, p2, p3)) * 0.06

print(calc_texes(10,20,30))

# пример функции return с множествами аргументами
def calc_texes1(*args):
    for x in args:
        print(f'Got paymnt = {x}')
    return sum((args)) * 0.06

print(calc_texes1(10,20,30, 40, 50, 11, 43, 90))

# пример функции return с множествами аргументами, ключ+значение
def save_players(**kwargs):
    for k,v in kwargs.items():
        print(f'Player {k} has rating {v}')

z = save_players(x1=1000, x2= 1555, x3=1700)
print(z)

# Пример args + kwargs
#def func_important(a,b,c,d, *args, **kwargs):

