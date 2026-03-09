import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF=pygame.display.set_mode((500,400),0,32)
anotherSurface=DISPLAYSURF.convert_alpha()
pygame.display.set_caption("New Sekai")

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

DISPLAYSURF.fill(WHITE)
spamRect=pygame.Rect(10,20,200,300)
pygame.draw.polygon(DISPLAYSURF,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.rect(DISPLAYSURF,RED,spamRect)
DISPLAYSURF.set_at((400,300),BLUE)

while True:#main game loop
    for event in pygame.event.get():#获取操作事件列表event
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()