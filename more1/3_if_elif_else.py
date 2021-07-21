# if если
# else другое
# elif (else if) если другое
# Управляющие конструкторы

#time = "Ночь"
#time = "День"
time ="hjgjh"

print("Прога раз.")
if time == 'Ночь':
    print('Ты псих? Сейчас же ночь!')
else:
    print('Сейчас. иди.')

time = "Утро"
print("\nПрога два.")
if time == 'Ночь':
    print('Ты псих? Сейчас же ночь!')
elif time == "Утро":
    print('Ты позавтракал?')
else:
    print('Сейчас. иди.')


time = "Утро"
print("\nПрога три.")
if time == 'Ночь':
    print('Ты псих? Сейчас же ночь!')
elif time == "Утро":
    print('Ты позавтракал?')
elif time == "День":
    print('Выпей воды...')
else:
    print('Сейчас. иди.')

print("\nПрога четыре.")
password = input('Введите пароль: ')
if password == '123':
    print('Пароль верный!')
else:
    print('Пароль не верный!')

