#In-place местные операторы
#Служат для сокращения написания кода
# +=
# -=
# *=
# /=
# %=


test = 10
test = test + 10
print(test)

test = 10
test += 10
print(test)

test = 10
# test = test - 5
test -= 5
print(test)

test = 7
# test = test * 2
test *= 2
print(test)

test5 = 25
# test = test / 5
test /= 5
print(test)

x = ' Test'
x *= 5
print(x)

# К сожелению в питоне нет такой фпшки как в других языка програмировния  test++ test--
# Но есть местные операторы
# test++
test = 10
test += 1
print(test)
# test--
test = 10
test -= 1
print(test)

