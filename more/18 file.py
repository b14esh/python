# менеджеры контекста
# with ... as
# в случие ошибки файл будет закрыт .close

with open('text.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1/' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write(line)

