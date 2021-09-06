from hero import *
from mod16 import pp


# ------------- MAIN
myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Alex", 4, "Humman")
mysuperhero = SuperHero("Mosia", 10, "elf", 5)
pp()
myhero1.show_hero()
pp()
myhero2.show_hero()
pp()
mysuperhero.show_hero()
pp()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.makemagic()
mysuperhero.show_hero()
mysuperhero.magic = 250
pp()