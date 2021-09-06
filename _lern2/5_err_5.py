# Пример выброса своей ошибки.....
import math

def calc_square(ab,ac, bc):
    if ab <=0 or ac <=0 or bc <=0:
        raise ValueError("One of the sides is less or equal to 0") # одно из числе меньше нуля
    p = (ab + ac + bc) /2
    s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    return s

square = calc_square(10, 10, 10)
print(square)


square = calc_square(-2, 8, 8) # ошибочка # не может быть сторона треугольнака отрецательной
print(square) # но тем немение код исполняется .....




