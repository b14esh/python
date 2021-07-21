# assert - утверждение \ условия
def exc(text):
    print(str(text) + '!')

exc('Hello world!')

def exc1(text):
    assert  text != '' # в этом случае если text != '' , пустой строке, выполняем код ниже print(str(text + '!')
                       # если строка будет пустой то выбросится ошибка AssertionError
    print(str(text) + '!')

exc1('Hello world!')
#exc1('')

def test(number):
       assert number > 0, "Number should be bigger than 0."
       print(str(number))
#test(-10)
test(10)