# Мы не раз печатали разные вещи, соединяя строки простым сложением. 
# Это не всегда удобно, особенно учитывая, что если попадутся числа, то их придется переводить в строки функцией str(). 
# Есть более красивый и удобный способ подставлять значения переменных внутрь строк.
# Метод .upper() в примере выше делает все буквы заглавными

name = 'Вася Пупкин'
age = 20
address = 'улица Пушкина, дом Колотушкина'
info = 'Имя: {}. Возраст: {}. Адрес: {}'.format(name, age, address)
print(info) 

data = ['Вася Пупкин', 20, 'улица Пушкина, дом Колотушкина']
info = 'Имя: {}. Возраст: {}. Адрес: {}'.format(*data)
print(info)

name = 'Вася Пупкин'
age = 20
address = 'улица Пушкина, дом Колотушкина'
info = f'Имя: {name.upper()}. Возраст: {age}. Адрес: {address}'
print(info)