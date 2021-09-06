# Защита атрибутов
# Защищенные атрибуты
# Приватные атрибуты

class Character():
    MAX_SPEED = 100 # Конастанты \ Постоянные значения \ Записываются заглавными буквами \ Сообщает програмисту что изменять не стоит

    def __init__(self, race, damage=10):
        self.__race = race # Обьевление приватного атрибута \ два символа "__" \ к атрибуту можно будет обратится по _Character__race
        self.damage = damage
        self._health = 100 # Обьявление защищенного атрибута одно нижние подчеркивание \ символ "_"

    def hit(self, damage):
        self.damage = damage

print(Character.MAX_SPEED)
Character.MAX_SPEED = 10
print(Character.MAX_SPEED)

c = Character('Elf')
c._Character__race = "Ork"
print(c._Character__race)

c._health = 0
print(c._health)