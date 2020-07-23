# операторы continue, break, else
# continue - пропускает одну итерацию
# break - прекращает дальнейшее выполнение, выходит из цикла
# else - срабатывает если условие if не сработало
pp = "\n\n#-------------------------------------------\n"
print(pp)
for j in 'hello world':
    if j == 'w':
        continue
    print(j * 3, end = '')


print(pp)

for j in 'hello world':
    if j != 'w':
        continue
    print(j * 2, end = '')

print(pp)

for j in 'hello world':
    if j == 'w':
        break
    print(j * 4, end = '')

print(pp)

for j in 'hello world':
    if j == 'a':
        break
    print(j , end='')
else:
    print("\nБуквы 'а' нету в строчке")

print(pp)

for j in 'hello world':
    if j == 'a':
        break
else:
    print("\nБуквы 'а' нету в строчке")

print(pp)