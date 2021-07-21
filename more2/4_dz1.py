#Парсинг римских чисел
#Написать функцию, которая принимает на вход строку - римское число, а
#возвращает это число в арабском виде. Например, если передаём "XV" - должна
#вернуть 15, если передаём "IV" - должна вернуть 4.
#Вот список римских символов и их отображение на арабские числа:
#I - 1
#V - 5
#X - 10
#L - 50
#C - 100
#D - 500
#M - 1000

numbers_r = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
numbers_a = ['1','5', '10', '50', '100', '500', '1000']
dict_numbers_r = dict(zip(numbers_r, numbers_a))
dict_numbers_a = dict(zip(numbers_a, numbers_r))

def rima_input():
    x = input("Введите цифру арабскую или римскую: ")
    rima(x)

def rima(x):
    if x in dict_numbers_r.keys():
        return print(f'Римская цифра \"{x}\". Арабская цифра \"{dict_numbers_r[x]}\".')
    elif x in dict_numbers_a.keys():
        return print(f'Арабская цифра \"{x}\". Римская цифра \"{dict_numbers_a[x]}\".')
    else:
        return print(f"Нет такого числа \"{x}\" в списке.")


rima_input()
