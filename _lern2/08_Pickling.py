# Pickling # Консервирование
# Срелизация файлов
# испоьзуется для сохронения данных

class Character():
    def __init__(self, race, armor=20, damage=10):
        self.race = race
        self.damage = damage
        self.health = 100
        self.armor = armor

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == 0

    #def __getstate__(self):

    def __setstate__(self, state):
        self.race = state.get('race', 'Elf')
        self.damage = state.get('damage', 10)
        self.armor = state.get('armor', 20)
        self.health = state.get('health', 100)

c = Character('Elf')
c.hit(10)
print(c.health)

import pickle
with open(r'game_state.bin', 'w+b') as f: # выгрузка в файл
    pickle.dump(c, f)


c = None # уничтожили данные в c
print(c)

with open(r'game_state.bin', 'rb') as f: # загрузка из файла
    c = pickle.load(f)
print(c.health)
print(c.__dict__)
