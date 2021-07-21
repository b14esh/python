# Двигаем картинку
import pygame
MAX_X = 800
MAX_Y = 600
#MAX_X = 2560
#MAX_Y = 1440
game_over = False
bg_color = (0,0,0) #RGB цвет фона сейчас черный


pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y)) # в окне
#screen = pygame.display.set_mode((MAX_X, MAX_Y)), pygame.FULLSCREEN # на весь экран
pygame.display.set_caption("My first Py game! :)")
# по умолчанию pygame понимает bmp картинки
print(pygame.image.get_extended())

x = 500
y = 100

myimage = pygame.image.load("1.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100)) # изменить размер изображения
# ---------------------- MAIN GAME LOOP
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN:
             x, y = event.pos

    screen.fill(bg_color)  # закрашиваем  фон
    screen.blit(myimage, (x, y)) # координаты картинки
    pygame.display.flip()