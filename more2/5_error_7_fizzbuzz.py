# Физбаз \ FizzBuzz
# Функции подаются числа.
# Если число делится на число 5 без остатка, выводится баз \ Buzz.
# Если число деллится на число 3 без остатка, выводится физ \ Fizz.
# Если число делится на числа 5 и 3 без остатка, выводится физбаз \ FizzBuzz.
# В отстальных случаях возращается пустая строка.
def get_reply(number):
    if number%5==0 and number%3==0:
        return 'FizzBuzz'
    elif number%3==0:
        return 'Fizz'
    elif number%5==0:
        return 'Buzz'
    else:
        return ''

x = 10
get_fizzbazz = get_reply(x)
print(f'Число {x} является: {get_fizzbazz}.')