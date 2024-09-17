import pygame
from random import randint

class Jogador:
    def __init__(self, largura, altura):
        self.x = 250
        self.y = 0
        self.largura = largura
        self.altura = altura
        self.distancia_do_movimento = 10
        self.cor = (200, 80, 199)

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
        if self.y > self.altura:
            self.y = 0
        elif self.y < 0:
            self.y = self.altura

        if self.x > self.largura:
            self.x = 0
        elif self.x < 0:
            self.x = self.largura

    def desenhar(self, window):
        ret_rosa = pygame.draw.rect(window, self.cor, (self.x, self.y, 40, 50))
        return ret_rosa