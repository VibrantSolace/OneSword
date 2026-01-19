import pygame
import math
import random
from Player import player

window_height = 720
window_width = 720
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game")

player_1 = player(1, (360, 680), screen)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #if keys[pygame.K_w]:
    #if keys[pygame.K_a]:
    #if keys[pygame.K_s]:
    #if keys[pygame.K_d]:

    screen.fill("White")

    player_1.draw()

    pygame.display.update()

pygame.quit()
