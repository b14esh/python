from hero import Hero
### Утащили все файл hero.py
#class Hero():
#    """ Class to create  Hero for our Game"""
#    def __init__(self, name, level, race):
#        """"Initiate our hero"""
#        self.name = name
#        self.level = level
#        self.race = race
#       self.health = 100
#    def show_hero(self):
#        """Print all parameters of this hero"""
#        #discription = (self.name + ", Level is: " + str(self.level) + ", Race is: " + self.race + str(self.health)).title()
#        discription = (f" {self.name}, Level is: {self.level},  Race is: {self.race}, Health is: {self.health}").title()
#        print(discription)
#
#    def level_up(self):
#        """ Upgrade Level of Hero"""
#       #self.level = self.level +1
#       self.level += 1
#
#    def move(self):
#         """ Start moving Hero"""
#         print("Hero " + self.name + " start moving...")
#
#    def set_health(self, new_health):
#        self.health = new_health
#---------------------------

# ------------- MAIN
myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Alex", 4, "Humman")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
#myhero1.health = 70 # не стоит так делать. лутше моздать  set_health
#myhero1.show_hero()
myhero1.move()
myhero1.set_health(60)
myhero1.show_hero()

