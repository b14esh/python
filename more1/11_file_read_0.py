# чтение / изменение / создание файлов файлов функция open()
# r - read / чтение
# w - /rewrite / write / create / перезапись / запись / создание
# a - append / добавление
# b - binary mode / 

file = open('11.txt', 'r', encoding='utf-8') # по умолчанию используется read \ можно 'r' не указывать
print(file.read())
file.close() # закрыть файл

