# Генератор не очень
import random

def randoms(min, max, n):
    return [random.randint(min,max) for _ in range(n)]

for r in randoms(10,30, 5):
    print(r)

# Генераторы # Ленивое вычисление
def randoms(min,max, n):
    for i in range(n):
        yield random.randint(min, max)
for r in randoms(10,30,5):
    print(r)

# Проверка
rand_sequence = randoms(1, 10, 10)
print(rand_sequence)

# По генератору можно пройтись только одни раз
for r in rand_sequence:
    print(r)

# Запихиваем в список
seq = list(randoms(1,10,5))
print(seq)


#
import itertools
def randoms(min, max, n):
    for i in range(n):
        yield random.randint(min, max)
rand_sequence = randoms(1,10,10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(f'{five_taken}')


#
def randoms(min, max):
    while True:
        yield random.randint(min, max)
rand_sequence = randoms(1, 10000)
five_taken = list(itertools.islice(rand_sequence, 5))
print(f'{five_taken}')


#
def read_line_be_line(file):
    """ Построчное чтение файла """
    while True:
        line = file.readline()
        if not line:
            break
        yield line
file = open(f'1.txt', 'r', encoding='utf-8')
for line in read_line_be_line(file):
    print(line.rstrip())

# Самы простой генератор
rand_seq = randoms(1,10)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)
n = next(rand_seq)
print(n)

#
my_list = [1,2,3,4]
squares = [x**2 for x in my_list]
print(squares)

for i in squares:
    print(i)


