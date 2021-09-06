# чтение / изменение / создание файлов файлов функция open()
# r - read / чтение
# w - /rewrite / write / create / перезапись / запись / создание
# a - append / добавление
# b - binary mode /

filename = input('Укажите файл: ')
file = open(filename, 'r', encoding='utf-8') # по умолчанию используется read \ можно 'r' не указывать
print(f"В данном файле {len(file.read())} символов.") # посчитаем количество символов
file.close() # закрыть файл