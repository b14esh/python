# декораторы
# позволяют завернуть выводл одной функции в другую
# !!! декораторы замедляют выводы функции
def decorator(func):
    def wrapper():
        print("Код до выполнения функции 1")
        func()
        print("Код, сработал после выполнения 1")
    return wrapper
def qwe(func):
    def wrapper():
        print("Код до выполнения функции 2")
        func()
        print("Код, сработал после выполнения 2")
    return wrapper
def test(func):
    def wrapper():
        print("Код до выполнения функции 3")
        func()
        print("Код, сработал после выполнения 3")
    return wrapper
@decorator
@qwe
@test
def show():
  print("Я обычная функция")

show()