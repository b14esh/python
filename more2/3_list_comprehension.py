# list
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

greeting = "Hello, world"
chars = []
for l in greeting:
    chars.append(l)
print(chars)

#list comprehension
chars = [l for l in greeting]
print(chars)

chars = [l for l in 'bla-bla-bla']
print(chars)

print('\n')

numbers = [n for n in range(0,11)]
print(numbers)

print('\n')

numbers = [n*n for n in range(0,11)]
print(numbers)

print('\n')

numbers = [n*n for n in range(0,11) if n%2!=0]
print(numbers)

print('\n')

len_in_centimeters = [88,888,6454,32,32]
len_in_inches = [(round(cm / 2.54,2)) for cm in len_in_centimeters]
print(len_in_centimeters)
print(len_in_inches)

print('\n')

ratings = [1520, 5454, 2454, 1000]
titles = ['GM' if x>=2500 else 'MM' for x in ratings]
print(titles)

print('\n')

# двойные циклы for
list1 = [2,4,-5,6,8,-2]
list2 = [2,-6,8,3,5,-2]
pairs = []

for x in list1:
    for y in list2:
        cur_sum = x + y
        if cur_sum == 0:
            pairs.append((x, y))
print(pairs)

print('\n')

# Похожие на list comprehension
pairs = [(x,y) if x+y ==0 else None for x in list1 for y in list2]
print(pairs)

for i in pairs:
    if i != None:
        print(i)

#!!!  Избигайте сложных ist comprehension