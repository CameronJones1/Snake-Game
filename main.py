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
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('basic game')
clock = pygame.time.Clock()
gray = (128,128,128)
screen.fill(gray)
head = pygame.Surface((30,30))
head.fill((0,255,0))
head_Rect = head.get_rect()


# Press the green button in the gutter to run the script.
while(1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                head_Rect.move_ip(0,-30)
            if event.key == K_DOWN:
                head_Rect.move_ip(0,30)
            if event.key == K_LEFT:
                head_Rect.move_ip(-30, 0)
            if event.key == K_RIGHT:
                head_Rect.move_ip(30, 0)

    screen.fill(gray)
    screen.blit(head,head_Rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
