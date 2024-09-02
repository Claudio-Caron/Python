import pygame, time
from pygame.locals import *
from sys import exit

PRETO = (0,0,0)
LARGURA = 640
ALTURA = 480
x=250
y=0

pygame.init()
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Survivor.IO')
clock = pygame.time.Clock()
distancia_do_movimento = 10

while True:
    window.fill(PRETO)
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                x=x-distancia_do_movimento
            elif event.key ==K_d or event.key == K_RIGHT:
                x=x+distancia_do_movimento
            elif event.key == K_s or event.key == K_DOWN:
                y=y+distancia_do_movimento
            elif event.key == K_w or event.key == K_UP:
                y=y-distancia_do_movimento'''
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x=x-distancia_do_movimento
    elif pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x=x+distancia_do_movimento
    elif pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y=y+distancia_do_movimento
    elif pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y=y-distancia_do_movimento
    
    pygame.draw.rect(window, (200, 80, 199), (x,y, 40, 50)) 
    pygame.display.update()
    if y > ALTURA:
        y=0
    elif y<0:
        y=ALTURA
    #y=y+1
    if x> LARGURA:
        x=0
    elif x<0:
        x=LARGURA
    
    