import pygame

# Inicializando módulos de Pygame
pygame.init()
PRETO = (0,0,0)
BRANCO =(255, 255, 255)
VERMELHO = (255, 0, 0)#Formato RGB
VERDE = (0,255,0)
AZUL = (0,0,255)


PI= 3.1415
# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((800, 600))
janela.fill(BRANCO)#recebe uma cor, retorna um  retângulo acaso precisar
fonte = pygame.font.Font(None, 48)
texto = fonte.render('Ola mundo!', True, BRANCO, AZUL)

janela.blit(texto, [30,150])
#desenhando figuras
pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)),0)
pygame.draw.circle(janela, AZUL, (300, 50), 20, 0)
pygame.draw.ellipse(janela, VERMELHO, (400, 250, 40, 80), 1)
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, VERMELHO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2, 2)
pygame.display.update()

pygame.display.set_caption('GAME')
deve_continuar = True

# Loop do jogo
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT(fechar ou tecla)
        if event.type == pygame.K_SPACE:
            deve_continuar = False
          
# Encerrando módulos de Pygame
pygame.quit()