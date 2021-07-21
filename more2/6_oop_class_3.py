# Свойства

class Character():
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.__race = race # Обьевление приватного атрибута \ два символа "__" \ к атрибуту можно будет обратится по _Character__race
        self.damage = damage
        self._health = 100 # Обьявление защищенного атрибута одно нижние подчеркивание \ символ "_"

    def hit(self, damage):
        self.damage = damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race
c = Character('Elf')
c._Character__race = "Ork"
print(c._Character__race)

c._health = 0
print(c._health)


print(c.health)
print(c.race)



#c.health  = -1000 # Не возвможнл изменить  \  будет ошибка AttributeError: can't set attribute
#c.race = "Z" # Не возвможнл изменить  \ будет ошибка AttributeError: can't set attribute