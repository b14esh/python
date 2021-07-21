#filename = '11.txt'
filename = input("введите желаемое имя файла: ")
text = input("Введите желаемый текст: ")
file = open(filename, 'w')
file.write(text)
file.close()