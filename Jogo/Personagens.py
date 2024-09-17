import pygame
from random import randint
from Const import LARGURA, ALTURA, DISTANCIA_DO_MOVIMENTO, ROSA, AZUL

class Jogador:
    def __init__(self):
        self.x = 250
        self.y = 0
        self.distancia_do_movimento = DISTANCIA_DO_MOVIMENTO
        self.cor = ROSA

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            self.x -= self.distancia_do_movimento
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            self.x += self.distancia_do_movimento
        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
            self.y += self.distancia_do_movimento
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            self.y -= self.distancia_do_movimento

        # Movimentação no eixo vertical e horizontal
        if self.y > ALTURA:
            self.y = 0
        elif self.y < 0:
            self.y = ALTURA

        if self.x > LARGURA:
            self.x = 0
        elif self.x < 0:
            self.x = LARGURA

    def desenhar(self, window):
        ret_rosa = pygame.draw.rect(window, self.cor, (self.x, self.y, 40, 50))
        return ret_rosa


class Inimigo:
    def __init__(self):
        self.x = randint(40, 600)
        self.y = randint(50, 430)
        self.cor = AZUL

    def desenhar(self, window):
        ret_azul = pygame.draw.rect(window, self.cor, (self.x, self.y, 40, 50))
        return ret_azul

    def resetar_posicao(self):
        self.x = randint(40, 600)
        self.y = randint(50, 430)