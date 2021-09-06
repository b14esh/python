# Классы....
# Класс описание сущности....
# Обьект экземпляр класса...

numbers = [1, 2, 3, 4]
print(type(numbers))

# Имя класса всегда пишется с заглавной буквы
#class Character():
#    def __init__(self, actual_race): # конструктор
#        self.character_race = actual_race
#unit = Character("Elf")
#print(type(unit))
#print(unit.character_race)



# Имя класса всегда пишется с заглавной буквы
#class Character():
#    def __init__(self, race): # конструктор
#        self.race = race
#
#unit = Character("Elf")
#print(type(unit))
#print(unit.race)


# Имя класса всегда пишется с заглавной буквы
class Character():
    def __init__(self, race, damage=10, armor=20): # конструктор
        self.race = race
        self.damage = damage
        self.armor = armor

#unit = Character("Elf", damage=20, armor=40)
unit = Character("Elf", 20, 40)
print(type(unit))
print(unit.race)
print(unit.damage)
print(unit.armor)