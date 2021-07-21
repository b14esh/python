# Циклы
#
print("Номер 0")
# обычное услове
test = True
if test:
    print('что-то')

print("\nНомер 1")
# while
# делай [что-то] пока [что-то]
# while бесконечный цыкл
test = True
while test:
    print('Привет')
    test = False # если это не поставить то он будет долбить бесконечно

print("\nНомер 2")
i = 1
while i <= 5:
    print(i)
    #i = i + 1
    i += 1

print("\nНомер 3")
i = 3
while i >= 0:
    print(i)
    #i = i - 1
    i -= 1

print("\nНомер 4")
i = 3
while i <= 0:
    print(i)
    i -= 1
print("Номер 4 конец")



x = 1
while x:
    print("loloolooo " + str(x))
    x += 1
    if x == 16:
        break