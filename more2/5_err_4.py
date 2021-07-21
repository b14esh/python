# пример ошибки....
import math

def calc_square(ab,ac, bc):
    p = (ab + ac + bc) /2
    s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    return s

square = calc_square(10, 10, 10)
print(square)


square = calc_square(-2, 8, 8) # ошибочка # не может быть сторона треугольнака отрецательной
print(square) # но тем немение код исполняется .....




