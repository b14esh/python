# коментарий, код не выполняется
# int число
# float число с точкой
# str строка
# input всегда возрощает строку

# 0
#num = input("ведите ваше имя: ")
#if num == "Test":
#    print("All is okay!, you name Test")

# 1
#num = input("ведите ваше имя: ")
#if num != "Test":
#    print("All is okay!, you name not Test")

# 2
#num = input("ведите число: ")
#if int(num) > 0:
#    print("вы ввели число больше 0")

# 3
#num = int(input("ведите число: "))
#if num > 0:
#    print("вы ввели число больше 0")

# 4
#num = input("ведите число: ")
#if float(num) > 0:
#    print("вы ввели число больше 0")
#elif float(num) < -10:
#    print("Вы ввели чилсло меньше -10")
#elif float(num) == -10:
#    print("Вы ввели чилсло -10")
#else:
#    print("Вы ввели число меньше нуля и больше -10")
#print("All okay")

# 5

#num = float(input("Введите положительное число: "))
#f num > 0:
#    print("Все ок вы вели положительное число: ", str(num))
#else:
#    print("Нужно ввести положительное число, а вы ввели: ", str(num))


# 6
#num = float(input("Введите положительное число: "))
#if num > 0:
#    print("Все ок вы вели положительное число: ", str(num))
#    if num == 10:
#         print("Вы ввели число равное 10")
#    elif num > 10:
#        print("Вы ввели число болше 10")
#    elif num <= 3:
#        print("Вы ввели число равное или меньшее 3")
#    else:
#       print("Вы ввели число меньше 10 но больше 3")
#else:
#    print("Нужно ввести положительное число, а вы ввели: ", str(num))

# 7
#name = input()
#A = 'Yes' if name != "Test" else 'No'
#print(A)

# 8
print("Если напечатаешь не Test, \n\tто ответ будет Yes, \n\tв остальных случаях No \n\tчто ты напечатаешь? ")
name = input("\tпечатай: ")
A = 'Yes' if name != "Test" else 'No'
print("\n\tТы напечатал:", name, "\n\tОтвет:", A, )


