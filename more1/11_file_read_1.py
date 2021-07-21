file = open('11.txt', 'r', encoding="utf-8")
#print(file.read()) # в utf-8 одна буква это два байта
print(file.read(2)) # показать перввые два байта / по факту покажит первые две букы / хз показывает буквы
print(file.read(1)) # показывает далее один символ
print(file.read(4)) #показывает далее четыре символа
#print(file.read(1024*100))
file.close()


file = open("11.txt", 'r', encoding="utf-8")
for i in range(3):
    print(file.read(8))

file.close()