print("---------------------------------------")
x = 25
if x == 25:
    print("YES you right")
else:
    print("No you are wrong")
print("---------------------------------------")
age = 20
if  (age <= 4):
    print(("You are baby, you age:  ") + str(age))
elif  (age >4) and (age < 12):
    print("You are kid, You age: " + str(age))
elif (age >= 12) and (age < 19):
    print("You age teenager, you age:  " + str(age))
else:
    print("You are old!")
print("---------------------------------------")

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

if 'lada' in all_cars:
    print("YES LADA is in the list")
else:
    print("No in list")
print("---------------------------------------")

all_cars = ['chrusler', 'dacia', 'bmw', 'KIA', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolett']
german_cars = ['bmw', 'vw', 'audi']

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + "is german cars")
    #else:
       # print(xxxx + "is not German cars")
print("---------------------------------------")