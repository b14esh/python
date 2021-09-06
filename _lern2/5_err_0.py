#def divide(a,b):
#    return a / b


def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

print(divide(10, 2))
print(divide(2, 0))
print("_____________________________________________")
def divide(a,b):
    try:
       return a / b
    except ZeroDivisionError as ex:
        print(f"Случилась ошибка: {ex}")

print(divide(1, 2))
print(divide(2, 0))







