# Picharm -> settings -> pluse -> search pygame -> install
# windows cmd -> python -m pip install --user pygame

#import pygame.examples.stars # установим игруху из примеров stars
#import pygame.examples.cursors
#pygame.examples.stars.main() # запуск игры
#pygame.examples.cursors.main()

import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    pygame.display.flip()
