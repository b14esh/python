# подключить из модуля одну функцию ко всем функцимя можно будет обращатся по имени
from random import  randint
print(randint(1, 10))

from math import sqrt
print(sqrt(25))

from math import sqrt, pi
print(sqrt(25))
print(pi)

# импортируется все из модуля т.е. ко всем функцимя можно будет обращатся по имени
from random import *
print(randint(1, 10))

from math import *
print(pi)