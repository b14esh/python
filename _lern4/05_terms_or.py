myname = input("Введите ваш логин: ")
mypass = input("Введите ваш пароль: ")
if(myname == 'Vi'  and mypass == '123') or (myname == 'mo' and mypass == '321'):
   result = 'Привет, ' + myname + '. Добро пожаловать!'
else:
   result = 'Я тебя не знать, давай пока!'
print(result)

