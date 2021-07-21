# Вывод своих ошибок
#raise # выбросить
print("1")
try:
    pogoda = 'Плохая'
    if pogoda == 'Плохая':
        raise TypeError
except TypeError:
    print("Поймано исключение TypeError")

print("\n2")
try:
    pogoda = 'Плохая'
    if pogoda == 'Плохая':
        raise TypeError('Тест')
except TypeError:
    print("Поймано исключение TypeError")

