#         0      1     2         3      4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada' ]

for x in cars:
    print(x.upper())

for x in range(1,6):
    print(x)

my_number_list = list(range(0, 10))
print(my_number_list)

for x in my_number_list:
    x = x * 2
    print(x)

my_number_list.sort(reverse=True)
print(my_number_list)
print(max(my_number_list))
print("Max number is: " + str(max(my_number_list)))
print("Min number is: " + str(min(my_number_list)))
print("Sum of lis: " + str(sum(my_number_list)))

#         0      1     2         3      4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada' ]

mycars = cars[1:4]
print(mycars)
mycars = cars[:4]
print(mycars)
mycars = cars[-3:]
print(mycars)
mycars = cars[-3:-1]
print(mycars)

#         0      1     2         3      4
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada' ]
# mycars = cars  - не правильно, соединение...
mycars = cars[:] # правильное - копирование массива