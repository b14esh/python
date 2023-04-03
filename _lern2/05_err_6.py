# Пример выброса своей ошибки.....

class InvalidTraingleError(Exception):
    """Raise when a triangle has invalid sides"""

import math

def calc_square(ab,ac, bc):
    if ab <=0 or ac <=0 or bc <=0:
        raise InvalidTraingleError("Ошибка!!!\nОдна из сторон треугольника меньше нуля!!!")
    p = (ab + ac + bc) /2
    s = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    return s

try:
    square = calc_square(-2, 8, 8) # ошибочка
except InvalidTraingleError as ex:
    print(ex)
else:
    print(square)


