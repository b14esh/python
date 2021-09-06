print("------- 0 -------\n")
file = open('11.txt', 'r', encoding='utf-8')
strings =  file.readlines()
print(strings)
file.close()

print("\n------- 1 -------\n")
file = open('11.txt', 'r', encoding='utf-8')
strings = file.readlines()
for string in strings:
    print(string)
file.close()

print("\n------- 2 -------\n")
with open('11.txt', 'r', encoding='utf-8') as f: # тут мы открываем файл на чтение и с помощь as задаем алиас f для все строки от "as" влево "with open('11.txt', 'r', encoding='utf-8')"
    print(f.read())
#file.close() - не требуется при with
