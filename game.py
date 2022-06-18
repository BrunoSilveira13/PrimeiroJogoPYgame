
import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load('sons/musica_de_fundo.mp3') 
pygame.mixer.music.play(-1)

son_colisao = pygame.mixer.Sound('sons/son_moeda.wav')

largura = 640
altura = 480
x = int(largura /2)
y = int(altura /2)

x_azul = randint(40,600)
y_azul = randint(50,430)

fonte = pygame.font.SysFont('arial', 30, False, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('GAME')
relogio = pygame.time.Clock()

while True: 
    relogio.tick(60) 
    tela.fill((0,0,0,))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 15
    if pygame.key.get_pressed()[K_d]:
        x = x + 15
    if pygame.key.get_pressed()[K_w]:
        y = y - 15
    if pygame.key.get_pressed()[K_s]:
        y = y + 15

    qua_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,50,50))
    qua_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,50,50))

    if qua_vermelho.colliderect(qua_azul):
        x_azul = randint(40,600)
        y_azul = randint(50,430)
        pontos = pontos + 1
        son_colisao.play()
    tela.blit(texto_formatado, (450,40))

    pygame.display.update()