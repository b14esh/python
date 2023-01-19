# Будь осторожен — скрипт в таком виде обшарит весь диск D. 
# Если он у тебя есть и там много хлама, то процесс может затянуться.

# Функция walk() модуля os принимает один обязательный аргумент — имя каталога. 
# Она последовательно проходит все вложенные каталоги и возвращает объект‑генератор, из которого получают:

# адрес очередного каталога в виде строки;
# список имен подкаталогов первого уровня вложенности для данного каталога;
# список имен файлов данного каталога.

import os
#for root, dirs, files in os.walk(r'D:'):
#for root, dirs, files in os.walk('.'):
for root, dirs, files in os.walk('/home'):
    for name in files:
        fullname = os.path.join(root, name)
        print(fullname)
        if('pass' in fullname):
            print('Бинго!!!')


