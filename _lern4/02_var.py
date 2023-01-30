print("Средняя продлолжительность жизни 73 года")
#В Python символ = применяется для присваивания значения переменной.
a = input("Сколько тебе лет?: ")
b = 73 - int(a)
print(f"Бухать тебе осталось примерно: {b} лует")

# В Python символ = применяется для присваивания значения переменной.

# Они могут содержать только следующие символы:
# буквы в нижнем регистре (от a до z);
# буквы в верхнем регистре (от A до Z);
# цифры (от 0 до 9);
# нижнее подчеркивание (_).
# Они чувствительны к регистру: thing, Thing и THING — это разные имена.
# Они должны начинаться с буквы или нижнего подчеркивания, но не с цифры.
# Python особо обрабатывает имена, которые начинаются с нижнего подчеркивания
# Они не могут совпадать с зарезервированными словами Python (их также называют ключевыми).

# Перед вами список зарезервированных1 слов:
# False await else import pass
# None break except in raise
# True class finally is return
# and continue for lambda try
# as def from nonlocal while
# assert del global not with
# async elif if or yield

# type(1), type(abc), type(99.9), type('9'), type("99")
# все что в ковычках всегда строка

# True
# Для ненулевых чисел эта функция вернет значение True
# bool(True), bool(1), bool(45), bool(-45)
# Нулевые значения преобразуются в значение False
# bool(False), bool(0), bool(0.0)


secret = 5
quess = 8
if quess < 7 :
   print("too low")
elif quess > 7 :
   print("too high")
elif quess == secret :
   print("just right")
else:
   print("me")



uuu  = ["вишня", "горошек", "арбуз", "тыква"]
print(uuu)
if uuu[0] == "вишня" or uuu[1] == "горошек":
   print(f"small : \n\t{uuu[0]} \n\t{uuu[1]} ")
letter = "ы"
if letter  in uuu[3]:
   print(f"yellow : \n\t{uuu[3]}  ") 
letter = "в"
if  letter  in uuu[0]:
    print(f"green : \n\t{uuu[0]} \n\t{uuu[1]} \n\t{uuu[2]}") 
