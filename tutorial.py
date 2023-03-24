import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

# start pygame
pygame.init()

pygame.display.set_caption("My Game")

#BG_COLOR = (255, 255, 255)
WIDTH , HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5


window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y , width, height):
        self.rect  = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


def get_background(name):
    image = pygame.image.load(os.path.join("assets", "Background", name))
    _, _, w, h = image.get_rect()
    tiles = []

    for i in range(WIDTH // w +1):
        for j in range(HEIGHT // h +1):
            pos = (i * w, j * h)
            tiles.append(pos)
    
    return tiles, image

def draw_background(window, tiles, image):  
    for pos in tiles:  
        window.blit(image, pos)

    pygame.display.update()
    
def main(window):
    #set up the clock   
    clock = pygame.time.Clock()
    background , image = get_background("Blue.png")

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw_background(window, background, image)

    pygame.quit()

if __name__ == "__main__":
    main(window)
