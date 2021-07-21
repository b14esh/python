# исключения
# rty - exept
#print(10 / 0) # делить на ноль не льзя
#print(int('qwerty')) # в число строку мы передать не можем
#print('2' + 1) #  строку с числом сложить не можем


### 0
#x = int(input())
#y = int(input())
#try: # что мы делаем
#    res = x / y
#except ZeroDivisionError: # Какую ошибку мы ищем
#    print("Вы ввели 0")  # что мы вернем
#    res = 0 # присвоим res = 0
#print(res)

### str

#try:
#    x = int (input())
#except ValueError:
#    print("Вы ввели не число")
#    x = 0
#print(x)

#### 0, str

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
try:
    res = x / y
except ZeroDivisionError:
   print("Вы ввели 0")
   res = 0
print(res)