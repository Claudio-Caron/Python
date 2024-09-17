import pygame
from pygame.locals import *
from sys import exit
from Const  import *
from J import *
from I import * 

class Jogo:
    def __init__(self):
        pygame.init()

        # Inicialização da janela
        self.window = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('Survivor.IO')

        # Inicialização de som
        self.musica_de_fundo = pygame.mixer.music.load(MUSICA_DE_FUNDO)
        pygame.mixer.music.play(-1)
        self.som_colisao = pygame.mixer.Sound(SOM_COLISAO)

        # Fonte e pontuação
        self.fonte = pygame.font.SysFont(FONTE, TAMANHO_FONTE, NEGRITO, ITALICO)
        self.pontos = 0

        # Carregar imagem
        #self.Jogador_direita = pygame
        self.imagem_fundo = pygame.image.load(IMAGEM_FUNDO)
        self.tamanho = pygame.transform.scale(self.imagem_fundo, (LARGURA, ALTURA))

        # Jogador e inimigo
        self.jogador = Jogador(LARGURA, ALTURA)
        self.inimigo = Inimigo(LARGURA, ALTURA)

        # Clock
        self.clock = pygame.time.Clock()

    def rodar(self):
        while True:
            self.window.fill(PRETO)
            self.window.blit(self.tamanho, (0,0))
            self.clock.tick(40)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            # Movimentação e colisão
            self.jogador.mover(self.window)
            self.ret_jogador = self.jogador.desenhar(self.window)
            
            self.ret_inimigo = self.inimigo.desenhar(self.window)

            if self.ret_jogador.colliderect(self.ret_inimigo):
                self.inimigo.resetar_posicao()
                self.pontos += 1
                self.som_colisao.play()

            # Renderizar texto de pontuação
            mensagem = f'Pontos : {self.pontos}'
            texto_formatado = self.fonte.render(mensagem, True, BRANCO)
            self.window.blit(texto_formatado, (450, 40))

            # Atualizar a tela
            pygame.display.update()

