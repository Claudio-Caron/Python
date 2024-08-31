import pygame, time

# Inicializando módulos de Pygame
pygame.init()
PRETO = (0,0,0)
BRANCO =(255, 255, 255)
VERMELHO = (255, 0, 0)#Formato RGB
VERDE = (0,255,0)
AZUL = (0,0,255)
AMARELO = (0,255,255)

LARGURAjanela = 800
ALTURAjanela = 600

PI= 3.1415



# Criando uma janela com o título “Olá, mundo!”
janela = pygame.display.set_mode((LARGURAjanela, ALTURAjanela))
janela.fill(PRETO)#recebe uma cor, retorna um  retângulo acaso precisar
fonte = pygame.font.Font(None, 48)



#desenhando figuras
'''pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.polygon(janela, PRETO, ((191, 206), (236, 277), (156, 277)),0)
pygame.draw.circle(janela, AZUL, (300, 50), 20, 0)
pygame.draw.ellipse(janela, VERMELHO, (400, 250, 40, 80), 1)
pygame.draw.rect(janela, VERDE, (20, 20, 60, 40), 0)
pygame.draw.arc(janela, VERMELHO, [250, 75, 150, 125], PI/2, 3*PI/2, 2)
pygame.draw.arc(janela, PRETO, [250, 75, 150, 125], -PI/2, PI/2, 2)'''
pygame.display.update()

pygame.display.set_caption('GAME')
deve_continuar = True

f1 = {'objRect': pygame.Rect(300, 80, 40, 80), 'cor': VERMELHO, 'vel': [0,-5], 'forma':'ELIPSE'}
f2 = {'objRect': pygame.Rect(200, 200, 20, 20), 'cor': VERDE, 'vel': [5,5], 'forma':'ELIPSE'}
f3 = {'objRect': pygame.Rect(100, 150, 60, 60), 'cor': AZUL, 'vel': [-5,5], 'forma':'RETANGULO'}
f4 = {'objRect': pygame.Rect(200, 150, 80, 40), 'cor': AMARELO, 'vel': [5,0], 'forma':'RETANGULO'}
figura = [f1, f2, f3, f4]
# Loop do jogo
while deve_continuar:
    # Checando eventos
    for event in pygame.event.get():
        # Se for um evento QUIT(fechar ou tecla)
        if event.type == pygame.QUIT:
            deve_continuar = False
texto = fonte.render('Start game', True, BRANCO, AZUL)
janela.blit(texto, [30,150])
texto = fonte.render('multiplayer', True, BRANCO, AZUL)
janela.blit(texto, [30,150])
texto = fonte.render('options', True, BRANCO, AZUL)
janela.blit(texto, [30,150])
texto = fonte.render('QUIT', True, BRANCO, AZUL)
janela.blit(texto, [30,150]) 
pygame.draw.rect(janela, VERDE, (295, 145, 233,233))#arrumar parâmetros

def mover(figura, dim_janela):
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]
    borda_esquerda = 0
    borda_superior = 0
    if figura['objRect'].top < borda_superior or figura['objRect'].bottom > borda_inferior:
        # figura atingiu o topo ou a base da janela
        figura['vel'][1] = -figura['vel'][1]
    if figura['objRect'].left < borda_esquerda or figura['objRect'].right > borda_direita:
        # figura atingiu o lado esquerdo ou direito da janela
        figura['vel'][0] = -figura['vel'][0]
    figura['objRect'].x += figura['vel'][0]
    figura['objRect'].y += figura['vel'][1]
# Encerrando módulos de Pygame
pygame.quit()