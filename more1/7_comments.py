test = 'yo!'
# коментарий
# еще коментарий
print(test) # тут коментарий
#print("hgfhfhfh") # закомент строка


# Строки докуметирования
def lol():
    """ Описание функции """
    print("LOL")
lol()

def lol1():
   ''' Описание функции '''
   print("LOL")
lol1()

# print(функция.__doc__) # и если Строки документации есть, о мы увидим их при выполнении print(функция.__doc__)
print(lol.__doc__)
print(lol1.__doc__)

#print(print.__doc__)
#print(str.__doc__)


