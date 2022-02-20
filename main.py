import sys
import pygame
import random


pygame.init()
pygame.display.set_caption('DVD Simulator')

clock = pygame.time.Clock()

screen_w = 750
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))

logo = pygame.image.load("DVD_logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (logo.get_width()*0.1, logo.get_height()*0.1))
logo_w = logo.get_width()
logo_h = logo.get_height()

x = screen_w/2
y = screen_h/2
vel_x = 0.2
vel_y = 0.2


while True:
    delta_time = clock.tick(60)
    x += vel_x * delta_time
    y += vel_y * delta_time

    hit_edge = False
    if x < 0:
        vel_x = abs(vel_x)
        hit_edge = True
    if x > screen_w - logo_w:
        vel_x = -abs(vel_x)
        hit_edge = True

    if y < 0:
        vel_y = abs(vel_y)
        hit_edge = True
    if y > screen_h - logo_h:
        vel_y = -abs(vel_y)
        hit_edge = True

    if hit_edge:
        logo.fill((255, 255, 255), special_flags=pygame.BLEND_MAX)
        c = pygame.Color(0, 0, 0)
        c.hsva = (random.randint(0, 360), 100, 65)
        logo.fill(c, special_flags=pygame.BLEND_RGBA_SUB)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    screen.blit(logo, (x, y))
    screen.blit(screen, (0, 0))
    pygame.display.update()