# Уже неоднократно вызывали разные функции — как встроенные в Python (например, print()), 
# так и из подключаемых модулей (например, urllib.request()). 
# Но что такое функция изнутри и как их делать самостоятел­но?

# Представь, что у тебя есть какой-то набор команд, которые нужно выполнять несколько раз, изменяя лишь входные данные. 
# Такие блоки команд обычно выносят в отдельные кусочки программы.

# В объектно ориентированном программировании функции являются методами какого-либо класса и пишутся через точку от его названия.

#s='ПриВет! я ПеремЕнная'
#print(s) # Функция
#s.lower() # Метод



# Для примера разберем простейшую функцию, которая будет принимать в качестве аргументов два любых числа и перемножать их, возвращая результат умножения. Назовем ее umn.

def umn(a,b):
    c = a * b
    return c


# Теперь, когда ты описал функцию, далее в этой же  программе  можно ее вызывать.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число '))
c = umn(a, b)
print (c)
