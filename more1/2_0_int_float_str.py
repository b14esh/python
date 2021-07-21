# Конвертация данных
test = 'Тестовая строка'
test2 = 2

print(test + str(test2))

# Для конвертации данных существует три функции
# int() - целые числа
# flot() - дробные числа
# str() - строки
# Вот так их можно использовать

print(test2)
print(float(test2))
print(int(float(test2)))
print(str(int(float(test2))))

print(int("3" + "4"))

print(float("210" * int("2")))