# Дебильный калькулято v2
# pip install colorama
from colorama import Fore, Back, Style
from colorama import init
init()

print( Fore.BLACK )
print( Back.CYAN )
what = input("Что делаем? (+, -,):")

print( Back.MAGENTA)


# Так как imput ввсегда возрощает строки то нам надо перделать строку в число
# Есть специальные функции bool(), float(), str(), int()
# float() весещственное / число с  точкой запятой
# int() целочисленное
a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print( Back.LIGHTYELLOW_EX)

# условия if
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
else:
    print("Выбрана не верная операция")

input() # что бы программа не закрывалась
# сборка в exe
# pip install pyinsatller
# Кладем наш скрипт в какуйнить папку
# pyinstaller -F calculate_2.py