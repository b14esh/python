# Dictionary - словарь
# Отличие от списка к значениям обращаемся по ключу
test = {
    "ключ1" : "значение1",
    "ключ2" : "значение2",
    "ключ3" : "значение3",
    "ключ4" : "значение4",
    "ключ5" : (1,2,3,4,5,6,7),
    "ключ6" : {"что": "оО", "Бу":"Нет1"},
    "zzzz" : False,
    "xxxx" : True,
     125 : "Сто двадцать пять"

}

print(test["ключ3"])
try:
    print(test["Тестовый ключ"])
except KeyError:
    print("Нет такого ключа")
finally:
    print(test["ключ6"]["Бу"])
    print(test["ключ5"][5])
    print(test["zzzz"])
    print(test["xxxx"])
    print(test[125])

# задача
prims = {1:2, 2:3, 4:7, 7:17}
print(prims[prims[4]])

# далее

if 125 in test:
    print("да существует")
else:
    print("нет не существует")


if 126 not in test:
    test.update({"126": "Сто двадцать шесть"})
    print("ок 126 нет, но сейчас добавим")

else:
    print("ура 126 есть")

print(test["126"])
