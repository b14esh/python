# декораторы
# позволяют завернуть выводл одной функции в другую
# !!! декораторы замедляют выводы функции
def decorator(func):
    def wrapper():
        print("Код до выполнения функции")
        func()
        print("Код, сработал после выполнения")
    return wrapper
@decorator
def show():
  print("Я обычная функция")

#show = decorator(show)
show()