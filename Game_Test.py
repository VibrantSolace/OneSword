import pygame
import math
import random

window_height = 720
window_width = 720
pygame.init()
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Game")

point_1 = [360, 360]
point_2 = [360, 340]
point_3 = [200, 340]
vel_3 = [0, 0]
dist = 160
vel_3_mag = 0
t_norm = [0, -1]

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
    
    vel_3[1] += 0.001

    dist = math.sqrt((point_2[0] - point_3[0]) ** 2 + (point_2[1] - point_3[1]) ** 2)
    t_norm = [-(point_2[1] - point_3[1]) / dist, (point_2[0] - point_3[0]) / dist] # tangential normal vector
    vel_3_mag = math.sqrt((vel_3[0] ** 2) + (vel_3[1] ** 2))
    vel_3 = [t_norm[0] * vel_3_mag, t_norm[1] * vel_3_mag]
    point_3[0] += vel_3[0]
    point_3[1] += vel_3[1]

    #print(vel_3, "vel")
    #print(t_norm, "norm")

    screen.fill("White")

    #pygame.draw.line(screen, (0, 0, 0), point_1, point_2, width=1)
    pygame.draw.line(screen, (0, 0, 0), point_3, point_2, width=1)

    pygame.display.update()

pygame.quit()
