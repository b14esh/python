# Программа для копирования текстового файла
filename1 = input('Введите название копируемого файла: ')
filename2 = input('Введите куда скопировать файл: ')
file1 = open(filename1, 'r')
file2 = open(filename2, 'w')

file2.write(file1.read())

file1.close()
file2.close()

print('Копирование заверщенно')