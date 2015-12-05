'''
Created on Nov 28, 2015

@author: Krishna Mudragada
'''

import pygame, sys

from pygame.locals import *

pygame.init()

WIDTH=400
HEIGHT=800
TITLE= "GAME_WINDOW"
DISPLAY = pygame.display.set_mode((int(WIDTH), int(HEIGHT)))
pygame.display.set_caption(TITLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
