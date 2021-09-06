# функции
# нужно дать имя например func
# можно не задавать параметры ()
# можно задать параметры x, a, b
#def func():
#def func(x,a,b)

def func(x):
    return x
print(func(23))


def func(x,a):
    return x + a
print(func(23, 12))
print(func('Hello', ' world!'))


def func(x,a):  # функции возврата
    res = x + a
    return res
print(func('Hello', ' world!'))


def func(x):  # вложенные функции
    def add(a):
        return x + a
    return add
test = func(100)
print(test(200))


def func(): # функция ничего не делает
    x = 34
    y = 45
    pass
print(func())


def func(r, w, y=2):  # аргумент по умолчанию записывают в конце
    res = r + w
    res *= y
    return res
print(func(2,4 ))  # не задали


def func(r, w, y=2):  # аргумент по умолчанию
    res = r + w
    res *= y
    return res
print(func(2,4, 3)) # изменили


def func1 (*args):   # * - говорит сколько угодно параметров, args просто название, выводится будет кортеж
    return args
print(func1(1,2,3,4,5,6,7,'sd'))

def func1 (**args):   # ** - говорит сколько угодно параметров, args просто название, выводится будет словарь
    return args
print(func1(a = 1, b = 2, c=6, z = 'sd'))
print(func1(short = 'dict', longer = 'dictonary'))


# lambda function  - анонимные функции
# записывается в одну строчку и выполняет одну операцию
add = lambda x, y: x * y
print(add(2,5))
print(add('q', 2))

print(((lambda  x, y : x*y) (2,6)))

fun = lambda *args: args
print(fun(2,56,78.56))
