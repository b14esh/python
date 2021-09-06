# Срез списка
#digits = [1,2,3,4,5,6,7,8,9,10]
#digits2 = digits[4]
#digits2 = digits[2:4]
#print(digits2)

#for i in range(10): # до 10
#    print(i)

# словарь = [от:до]

digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[2:5] # от 2 до 5
print(digits2) # вывод будет 3,4,5

sqs = [0,1,4,9,16,25,36,49,64]
print(sqs[4:7]) # от 4 и до 7 # вывод будет 16,25,36

# пропуск индекса срезов
digits = [1,2,3,4,5,6,7,8,9,10]
print(digits[:3]) # от начала и до третьего сивола
print(digits[3:11]) # от 3 и до 11
print(digits[3:]) # от третьего символа и до конца

# шаг индексирования
digits = [1,2,3,4,5,6,7,8,9,10]
print(digits[::2])
print(digits[::3])
print(digits[::5])

digits2 = range(2, 101)[::2]
for i in digits2:
    print(i)


sqs = 0,1,4,9,16,25,36,49,64,81
print(sqs[1::4])


# отрецательные значения \ неготивные значения
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[-3] # получить третию цифру с конца
print(digits2)
digits2 = digits[-4:-1]
print(digits2)

# ревирс
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[::-1]
print(digits2)
# перевернуть обратно
digits = [1,2,3,4,5,6,7,8,9,10]
digits2 = digits[::-1][::-1]
print(digits2)



sqs = 0,1,4,9,16,25,36,49,64,81
print(sqs[7:5:-1])

sqs1 = 81,64,49,36,25,16,9,4,1,0
print(sqs1[-8:-6])


sqs = 1,2,3,4,5,6,7,8,9,10
print(sqs[7:5:-1])
sqs = 10,8,9,7,6,5,4,3,2,1
print(sqs[-7:-5])
