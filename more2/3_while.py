# До тех пор пока
x = 0
while x < 3:
    print(f' x equals {x}')
    x+=1

print('\n')

x = 0
while x <3:
    print(f' x equals {x} ZZZ')
    x += 1
else:
    print('Condition is not met')

print('\n')

vals = [1,2,3,4,5,6,7,8,9]
sum = 0
for v in vals:
    if v % 2 == 0:
        continue
    else:
        sum += v
    if sum > 10:
        break
print(sum)

print('\n')

for v in vals:
    pass