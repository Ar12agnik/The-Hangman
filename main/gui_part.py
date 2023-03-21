#agnik part
import pygame as pg
import sys
pg.init()
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
screen=pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
screen.fill((255, 255, 255))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
            
        

        pg.display.update()