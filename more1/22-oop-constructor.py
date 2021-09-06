# кострукторы, переопределение методов
class Person:
    name = "Ivan"
    age = 10
    def __init__(self, name, age):  #коструктор
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1
    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

igor = Student("Иван", 70)
igor.set ("Игорь", 19, 2)
print(f"{igor.name} {igor.age} {igor.course}")

vlad = Person("Влад", 25)
print(f"{vlad.name} {vlad.age}")

ivan = Person("Иван", 70)
print(f"{ivan.name} {ivan.age}")
