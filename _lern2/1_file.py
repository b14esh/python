# Запишим байты в файл и прочитаем его...
# int - это байты
mass = [12, 255, 9, 33,] # создали список байтов

# записали в файл
with open(r'file.bin', 'wb') as file:  # with заботится о закрытии файла  file.close не требуется
    file.write(bytes(mass))

# прочитали из файла
with open(r'file.bin', 'rb') as file:
    data = file.read()
    for b in data:
        print(int(b))

