def divide(a,b):
    try:
       return a / b
    except ZeroDivisionError as ex:
        print(f"an error occured: {ex}")
    except:
        print("unknown error occured!")

def pp():
    print("XXX-----XXX--------------xxx")
pp()
print(divide(1, 2))
pp()
print(divide(2, 0)) # деление на ноль :)
pp()
divider = input("input number: ") # деление числа на строку :)
divide(4,divider)
