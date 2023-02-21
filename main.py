import pygame
from settings import *

pygame.init()
sc = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    sc.fill(BLACK)

    pygame.draw.circle(sc, GREEN, player_pos,12)

    pygame.display.flip()
    clock.tick()
