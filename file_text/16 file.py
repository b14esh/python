# работа с файлами
#'r'	открытие на чтение (является значением по умолчанию).
#'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
#'x'	открытие на запись, если файла не существует, иначе исключение.
#'a'	открытие на дозапись, информация добавляется в конец файла.
#'b'	открытие в двоичном режиме.
#'t'	открытие в текстовом режиме (является значением по умолчанию).
#'+'	открытие на чтение и запись

#f = open('text.txt', 'rt')
#f = open('text.txt', 'rb')
def pp():
    az = "####-----------------####"
    print(az)
    return pp

pp()
f = open('text.txt')
print(f.read()) # выведет все содержимое
f.close()

pp()
f = open('text.txt')
print(f.read(1))  # выведет один символ
f.close()

pp()
f = open('text.txt')
print(f.read(10)) # выведет десять символов
f.close()

pp()
f = open('text.txt')
for line in f:
    print(line) # будем выводить построчно все на экран
f.close()

pp()

f = open('text.txt')
for line in f:
    print(line.strip()) # будем выводить построчно все на экран и удалим пустые строки
f.close()

pp()

f = open('text.txt', 'w') # !!! перезапись файла
f.write('Hi, write it\' me! \nTEST 21')
f.close()
pp()
