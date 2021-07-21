import sys
#filename = "myfile.txt" #правильно имя
filename = "myfile_error.txt" # ошиблись в имени файла :)
#myfile  = open(filename, mode='r', encoding='utf_8')
#print(myfile.read())

while True:
  try:
    print("Inside Try")
    myfile  = open(filename, mode='r', encoding='utf_8')
  except Exception:
    print("Inside EXCEPT")
    print(">>>>> Error Found! :( <<<<<<<<<<<<<<")
    #sys.exit()  #завершит дальнейшие выполнение программы
    print(sys.exc_info()[1])
    filename = input("Enter correct file name!: ")
  else:
    print("Inside ELSE")
    print(myfile.read())
    sys.exit() # если тут не поставить выход то будет бесконечный цыкл :)
  finally:
    print("Inside FINALLY")
    print("=============EOF==========================")
