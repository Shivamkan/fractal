import sys
import pygame

width = 600
height = 600
screen = pygame.display.set_mode((width, height))


def handleInput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def make(rect, depth):

    width = round(rect.width / 3)
    height = round(rect.height / 3)
    x = rect.x + width
    y = rect.y + height
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))

    if depth == 1:
        return None

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            make(pygame.Rect(rect.x + i * width, rect.y + j * height, width, height), depth - 1)


while True:
    make(pygame.Rect(0, 0, width, height), 5)
    handleInput()
    pygame.display.flip()
