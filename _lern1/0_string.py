# комментарий
# STRING
# строки
# строку определяют ковычки
# двойные ковычки 

print("Я строка в двойных ковычках.")
# одинорные ковычки \ апостроф

print('Я строка в одинарных ковычках.')

# использование экранирования
print("Я строка в двойных ковычках.\"когвычка в ковычках\".")

# перенос строк
print("Первая строка. \nВторая строка.\nТреться строка.")

# перенос строк без \n с использованием спец комбинации '''
print('''Первая строка. 
Вторая строка.
Треться строка.
и еще куча строк
''')


# обьеденение строк \ Конкатенация
# допустим у вас есть две строки "Строка номер один," и " cтрока номер два"
# их нужно вывести функцией print()
# для этого есть сец символы.
# Плюс
print( "Строка номер один," + " cтрока номер два.") # обрати внимание при плюсе пробел я поставил во второй строке
# Запятая ,
print( "Строка номер один,", "cтрока номер два.")   # орати внимание пробел сам релеазовался

# И еще раз про строки
# !!!Запомни Все что в ковычка это строки
# !!!Не важно в каких ковычках, одинар или двойных, в python это строки
print("2" + "2")
#print(2 + '2' + 6 + "7") # вот сколько тут будет =) а вот нисколько не будет. будет ошибка TypeError
#!!! Нельзя выполнять конкантенацию строк и цифор без преобразования

# Умножение строк
print('Привет ' * 5)
print('7' * 3)