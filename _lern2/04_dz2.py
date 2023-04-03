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

romans = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
def parse_roman(roman):
    result=0
    for i, c in enumerate(roman):
        #if i+1 < len(roman) and romans[roman[i]] < romans[roman[i+1]]:
        #    result -=romans[roman[i]]
         if i+1 < len(roman) and romans[c] < romans[roman[i+1]]:
            result -= romans[c]
         else:
            #result += romans[roman[i]]
            result += romans[c]
    return  result
print(parse_roman('I')==1)
print(parse_roman('II')==2)
print(parse_roman('III')==3)
print(parse_roman('IV')==4)
print(parse_roman('V')==5)
print(parse_roman('VI')==6)
print(parse_roman('VII')==7)
print(parse_roman('X')==10)
print(parse_roman('XIV')==14)
print(parse_roman('L')==50)
print(parse_roman('C')==100)
print(parse_roman('D')==500)
print(parse_roman('M')==1000)