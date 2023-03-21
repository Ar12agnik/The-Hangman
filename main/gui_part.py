#agnik part
import pygame as pg
import sys
pg.init()
WINDOW_WIDTH = 788
WINDOW_HEIGHT = 493

z=int(input("enter a number: "))
def gui_screen(z):
    screen=pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    screen.fill((255, 255, 255))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            x=pg.image.load(f'main\\{z}.png').convert_alpha()
            screen.blit(x,(0,0))
                
            

            pg.display.update()
if __name__=='__main__':
    gui_screen(z)