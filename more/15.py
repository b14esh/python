# Исключения try, except, finnaly, else
try:
    x = int (input())
except ValueError:
    print("Вы ввели не число")
    x = 0
try:
    y = int (input())
except ValueError:
    print("Вы ввели не число")
    y = 0
else: # выполнится если ошибок не было
    print("Все верно")
finally: # всегда выполняется со 100% вероятностью
    print("Выполнится 100%")

try:
    res = x / y
except ZeroDivisionError:
   print("Вы ввели 0")
   res = 0
print(res)