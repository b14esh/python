class Hero():
    """ Class to create  Hero for our Game"""

    def __init__(self, name, level, race):
        """"Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters of this hero"""
        # discription = (self.name + ", Level is: " + str(self.level) + ", Race is: " + self.race + str(self.health)).title()
        discription = (f" {self.name}, Level is: {self.level},  Race is: {self.race}, Health is: {self.health}").title()
        print(discription)

    def level_up(self):
        """ Upgrade Level of Hero"""
        # self.level = self.level +1
        self.level += 1

    def move(self):
        """ Start moving Hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """ Class create super Hero"""

    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        #self.magic = 100 # __magic - два андерскора __ перед magic запретит инкапсуляцию.... изменятся будет только из класса
        self.__magic = 100

    def makemagic(self):
        """Use magic"""
        #self.magic -= 10
        self.__magic -= 10

    def show_hero(self):
        discription = (
            #f" {self.name}, Level is: {self.level},  Race is: {self.race}, Health is: {self.health}, Magic is: {self.__magic}").title()
            f" {self.name}, Level is: {self.level},  Race is: {self.race}, Health is: {self.health}, Magic is: {self.__magic}").title()
        print(discription)