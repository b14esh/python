input_file = "text.txt" # файл который будем читать
output_file =  "outfile.txt" # файл в который будем записывать
look_for = "TEST" #что будем икать

myfile1  = open(input_file)  #Это строка открывает файл на чтение
myfile2  = open(output_file, 'a') #Эта строка позволит дописывать в файл (mode='a')

for num, line in enumerate(myfile1,1):  #  Читается файл text.txt и записывается в другой файл outfile.txt  искомую строку со словом TEST
    if look_for in line:
      print("Line № " + str(num) + " : " + line.strip())
      myfile2.write(f"look for: {line}")
myfile1.close()
myfile2.close()
