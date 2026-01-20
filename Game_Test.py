
import pygame
import math
import random


def get_dist(first, second):
    return math.sqrt((first ** 2) + (second ** 2))


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
t_unit = [0, -1]

screen.fill("white")
a = 0
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


    t_unit = [-(point_2[1] - point_3[1]) / dist, (point_2[0] - point_3[0]) / dist] # tangential unit vector
    if (vel_3[1] > 0 and t_unit[1] <= -0.1) or (vel_3[1] < 0 and t_unit[1] >= 0.1):   #Maybe just check if the angle is within 180 degrees
        t_unit[1] *= -1                                                               #using sin
        t_unit[0] *= -1
    elif (vel_3[0] > 0 and t_unit[0] <= -0.1) or (vel_3[0] < 0 and t_unit[0] >= 0.1):
        t_unit[1] *= -1
        t_unit[0] *= -1
    vel_3_mag = math.sqrt((vel_3[0] ** 2) + (vel_3[1] ** 2))
    vel_3 = [math.trunc( t_unit[0] * vel_3_mag * 100000) / 100000, math.trunc(t_unit[1] * vel_3_mag * 100000) / 100000]
    point_3[0] += vel_3[0]
    point_3[1] += vel_3[1]

    if abs(vel_3_mag) > a:
        print(vel_3_mag)
        a = vel_3_mag

    dist = get_dist(point_2[0] - point_3[0], point_2[1] - point_3[1])

    if dist != 160:
        new_x = (point_2[0] - point_3[0]) / dist
        new_y = (point_2[1] - point_3[1]) / dist
        new_x *= 160
        new_y *= 160
        point_3[0] = point_2[0] - new_x
        point_3[1] = point_2[1] - new_y
        dist = 160
    
    screen.fill("White")

    #pygame.draw.line(screen, (0, 0, 0), point_1, point_2, width=1)
    pygame.draw.line(screen, (0, 0, 0), point_3, point_2, width=1)
    pygame.draw.circle(screen, (0, 0, 0), point_3, 5, 5)

    pygame.display.update()

pygame.quit()
