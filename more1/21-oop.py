# ООП наследование, инкапсуляция, полиморфизм
# инкапсуляция _ __ , _name, __name
class Person:
    name = "Ivan"
    age = 10
    def set(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    course = 1

igor = Student()
igor.set("Игорь", 19)
print(f"{igor.name}  {igor.age} {igor.course}")

vlad = Person()
vlad.set ("Влад", 25)
print(f"{vlad.name} {vlad.age}")

ivan = Person()
ivan.set ("Иван", 70)
print(f"{ivan.name} {ivan.age}")
