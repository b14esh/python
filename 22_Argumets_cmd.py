# cmd 22_Argumets_cmd.py arg1 arf2 arg3 x yui
import sys
#print("hello")
#print(sys.argv)
#print(sys.argv[1:])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print(sys.argv[-1])
#print(sys.argv[-2])
#print(sys.argv[0])


def pp():
    print("#----------------------------------------------------------------")

pp()


x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this program: enter argument for pogram \n\t myprogram.py /? for help \n\t myprogram.py YO  print HELLO ")
        #print("Total arg enter: " + str(x))
    elif sys.argv[1] == "YO":
          print("\n\t HELLO")
    print("Argument enter: " + str(sys.argv[1:]))
    #print(sys.argv)
else:
    print("Not enter arguments")
pp()

x = len(sys.argv)
if x > 1:
    if sys.argv[1] == "/?":
        print("Help requested")
        print("Usage of this program: enter argument for pogram \n\t myprogram.py /? for help \n\t myprogram.py YO  print HELLO ")
        print("Argument enter: " + str(sys.argv[1:]))
else:
    print("Not enter arguments")

pp()

# а теперь прикольное выполнение команд OS из python
import os # позволяет использовать встроенные программы текущей ОС
import sys
os.system("dir") # выполнит команду dir из ОС Windows
# os.system("dir > cmd_dir.txt") # перенаправить вывод команды dir в файл cmd_dir.txt
# os.mkdir("mydir") # создать каталог средствами python и назвать ее mydir
os.system("ping ya.ru > pingyaru.txt") # запустить ping windows пинговать ya.ru и записать результат в файл pingyaru.txt
sys.exit()
