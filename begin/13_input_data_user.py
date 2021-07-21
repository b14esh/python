#name = input("Please enter your name: ")
#print("Privet " + name)
#print(f" Привет {name} !")
#!!! input всегда читает строки. НЕ ЦИФРЫ!!!!
pp = "-----------------------------------------------------------"
print(pp)
#num1 = input("Enter X: ")
#num2 = input("Enter Y: ")
######summa = num1 + num2
######Будет ошибка. Так как input  читает и подстовляет строки.
# требуется выполнить int (преоброзование строки в число)
#summa = int(num1) + int(num2)
#print(summa)
print(pp)
message = ""
#while message != 'secret':
#    message = input("Enter Password: ")
#    print(message + "Password Not Correct")
print(pp)
#while True:
#     message = input("Enter Password: ")
#     if message == 'secret' : break
#     print(message + "  <<<< Password Not Correct")
print(pp)
mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish: ")
    mylist.append(msg)
print(mylist)
