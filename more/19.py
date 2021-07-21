# модули
# https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%B0%D1%8F_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B0_Python
import math
print(math.e)
print(math.pi)
print(math.cos(1))

# import time, os # работать будет но считается дурным тоном, лутше импортировать по одно библиотеке
import time
import os

print(time.time())

print(os.getcwd()) # путь скрипта
print(os.name)
print(os.getlogin())
print(os.getpid())

import random as r # обращатся к random как к r
print(r.random())

import modpp
modpp.pp()

try:
   import module
except ImportError:
    print("Модуля не существует")

module.hi()
print(module.add(45,20))

modpp.pp()

try:
   import module as m
except ImportError:
    print("Модуля не существует")


m.hi()
print(m.add(100,100))

modpp.pp()


from modpp import pp
pp()

from module import hi as h, add as a
h()
print(a(45,15))
pp()