# https://docs.python.org/3/tutorial/errors.html - ошибки и описание


def get_int():
    while True:
        try:
            reply = int(input('Enter a number: '))
            #break # все ок завершаем обработку
            return reply
        except:
            print('Not a number!. try again')
            continue # продолжаем цикл


number = get_int() # допустим цыкл в переменную
print(number)

