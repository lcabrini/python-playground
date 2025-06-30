#! /usr/bin/env python

import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    screen.fill("black")
    pygame.display.flip()
    clock.tick(60)