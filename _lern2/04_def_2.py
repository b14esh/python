def square(*args):
    return [x*x for x in args]

result = square(1,2,3,4,5)
print(result)

def triple(*args):
    return [x*3 for x in args]

result = triple(1,2,3,4,5)
print(result)


# функция map()
def square1(number):
    return number * number
numbers = [1,2,3,4,5]

mapped_seq = map(square1, numbers)
print(mapped_seq)
print(type(mapped_seq))

# map распечатать
for x in mapped_seq:
    print(x)

# map или вот так вот
for x in map(square1, numbers):
    print(x)

# map  list
mapped_list = list(map(square1, numbers))
print(mapped_list)


# Функция filter()
def is_adult(age):
    return age >=18
ages = [14,18,21,30]
print(filter(is_adult, ages))
print(type(filter(is_adult, ages)))
filter_list = list((filter(is_adult, ages)))
print(filter_list)


# лямбды # анонимные функции
# В лябдо вырожении нельзя написать несколько строчек кода
# Чаще всего лябды используются с функциями filter() и map()
# Фишка лябды записать код в одну строку
ages = [14,18,21,30]
is_adult = lambda age: age >=18
print(is_adult)

lambda_list = list(filter(lambda age: age >=18, ages))
print(lambda_list)

#лябды несколько значений
multiplier = lambda x,y: x*y
z = multiplier(2,3)
print(z)
