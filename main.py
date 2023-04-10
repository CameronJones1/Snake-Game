import pygame
from sys import exit
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,

)

pygame.init()
display_width = 400
display_height = 500
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('basic game')
clock = pygame.time.Clock()
gray = (128,128,128)
gameDisplay.fill(gray)
head = pygame.draw.rect(gameDisplay,(0,255,0),pygame.Rect(30, 30, 30, 30))


# Press the green button in the gutter to run the script.
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                print("up")
            if event.key == K_DOWN:
                print("Down")
            if event.key == K_LEFT:
                print("Left")
            if event.key == K_RIGHT:
                print("Right")



    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
