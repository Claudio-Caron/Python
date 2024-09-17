from random import randint
import pygame



class Inimigo:
    def __init__(self, largura, altura):
        self.x = randint(40, 600)
        self.y = randint(50, 430)
        self.cor = (0, 150, 255)
        self.largura = largura
        self.altura = altura

    def desenhar(self, window):
        ret_azul = pygame.draw.rect(window, self.cor, (self.x, self.y, 40, 50))
        return ret_azul

    def resetar_posicao(self):
        self.x = randint(40, 600)
        self.y = randint(50, 430)
