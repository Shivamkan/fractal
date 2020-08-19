import sys
import pygame
from math import sqrt

width = 600
height = 600
screen = pygame.display.set_mode((width, height))


def handleInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def make(triangle, depth):
        x, y, a = triangle
        A = (x, y)
        B = (x + a, y)
        C = (x + a / 2, y + sqrt(3) / 2 * a)

        a1 = (x + 3 * a / 4, y + sqrt(3) / 4 * a)
        b1 = (x + a / 4, y + sqrt(3) / 4 * a)
        c1 = (x + a / 2, y)

        length = a /2

        pygame.draw.polygon(screen, (255, 255, 255), [A, B, C], 1)

        if depth == 1:
            return

        make((b1[0], b1[1], length), depth - 1)
        make((A[0], A[1], length), depth - 1)
        make((c1[0], c1[1], length), depth - 1)





while True:
    make((0, 0, min(width, height)), 7)
    handleInput()
    pygame.display.flip()
