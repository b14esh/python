# countinue заставляет ничего не делать циклу
# В приере получам четные числа
print("Программа получаем четные числа.")
number = 0
while number <= 10:
    number += 1
    if (number % 2) != 0: # Если модуль чила не равен 0. Ничего не делать. пропускаем
        continue
    print("Четное число : " + str(number))
print("Программа завершина.")

print("\nПрограмма получаем нечетные числа.")
number = 0
while number <= 9:
    number += 1
    if (number % 2) == 0: # Если модуль чила не равен 0. Ничего не делать. пропускаем
        continue
    print("Четное число : " + str(number))
print("Программа завершина.")