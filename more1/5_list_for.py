# for для списков достаточно новая фишка и более предпочтительна перед while
numbers = [1, 2, 3, 4, 5]
for element in numbers:
    print(str(element) + '!')

for test3 in numbers:
    print(test3)


for test in range(15):
    print('Привет!')


# WTF ?!
list = [1, 1, 2, 3, 5, 8, 13]
print(list)
print(list[4])
print(list[list[4]])

# ответ
# на задаче: list[list[4]],
# сперва у нас делается : list[4],
# по индексу это у нас число 5,
# затем это число преобразовывается в индекс 5,
# по индексу это число 8!
# (а выглядело бы это так:
# 1) list[list[4]] ,
# 2) list[5])
# 8
