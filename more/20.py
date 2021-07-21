# ООП - Объектно-ориентированное программирование
# классы -> обьекты -> методы, события, свойства
from modpp import pp
#class Person:
#    name = "Ivan"
#    age = 10

#vlad = Person()
#vlad.name = "Влад"
#ivan = Person()
#ivan.age = 45
#print(vlad.name)
#print(ivan.name)
#print(ivan.age)
pp()
# Вот так

class Person:
    name = "Ivan"
    age = 10
    def set(self, name, age):
        self.name = name
        self.age = age

vlad = Person()
vlad.set ("Влад", 25)
print(vlad.name + " " + str(vlad.age))

ivan = Person()
ivan.set ("Иван", 70)
print(ivan.name + " " + str(ivan.age))
pp()