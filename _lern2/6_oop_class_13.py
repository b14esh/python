# Функция super() - позволяет не вызывать джважды вложенные классы, и избежать проблемы двойной иницилизации вызова классов
# МРО
# Функция super() - гарантирует последовательность вызовов

# Смертельный ромб...
class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        #super().set_health(health)
        Animal.set_health(self, health)
        print('set in carnivour')

class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        #Animal.set_health(self, health)
        print('set in mammal')

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        super().set_health(health)
        #Mammal.set_health(self, health)
        #Carnivour.set_health(self, health)


        print('set in dog')

dog = Dog() # Создадим экземпляр dog
dog.set_health(10) # Вызов