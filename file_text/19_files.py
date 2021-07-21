#input_file = "../myfile.txt"

# mode -  есть несколько режимов открытия файла
# r  - read - чтение
# w  - write - запись
# a  - append - добовлять
# r+ - read pluse - читать и писать

# encoding
# кодировка
# utf8
# ascii
from mod16 import pp
pp()
input_file = "myfile.txt" # файл который будем читать
output_file = "outfile.txt" # файл в который будем записывать
password_to_look_for = "Hyponi111"


#myfile1  = open(input_file, mode='r', encoding='ascii')
myfile1  = open(input_file, mode='r', encoding='utf_8') # Это строка открывает файл на чтение
myfile2  = open(input_file, mode='r', encoding='utf_8') # Это строка открывает файл на чтение
myfile3  = open(input_file, mode='r', encoding='utf_8') # Это строка открывает файл на чтение
myfile4  = open(input_file, mode='r', encoding='utf_8') # Это строка открывает файл на чтение
#myfile5  = open(output_file, mode='w', encoding='utf_8') # Эта строка создает новый файл для записи, если файл закрыт то он будет перезаписан
myfile5  = open(output_file, mode='a', encoding='utf_8') # Эта строка позволит дописывать в файл (mode='a')
#print(myfile1.read()) # прочитаем файл
for line in myfile1:  #  прочитаем файл построчно, скажим всем привет, выволим на экран, strip обрежит лишнии пробелы
    print("Hello " + line.strip())
pp()

for num, line in enumerate(myfile2,1):  #  прономеруем
    print("Line № " + str(num) + " : "+ line.strip())
myfile2.close()
pp()

for num, line in enumerate(myfile3,1):  #  распечатаем если есть lolol2
    if "lolol2" in line:
      print("Line № " + str(num) + " : "+ line.strip())
pp()
myfile3.close()
for num, line in enumerate(myfile4,1):  #  Читается файл и записывается в  другой файл искомая строка со словом Hyponi111
    if "Hyponi111" in line:
      print("Line № " + str(num) + " : "+ line.strip())
      myfile5.write(f"Found password: {line}")
myfile4.close()
myfile5.close()

pp()