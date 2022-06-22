import os
import pygame
from pygame.locals import *
from sys import exit
from random import randint

os.system('cls')
nome = input('Nome > ')
email = input('Email > ')
arquivo = open('historicos.txt','a' )
arquivo.write(f'Nome > {nome}\n')
arquivo.write(f'Email > {email}\n')
arquivo.write('\n')
arquivo.close()

pygame.init()

pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load('sons/musica_de_fundo.mp3') 
pygame.mixer.music.play(-1)

son_colisao = pygame.mixer.Sound('sons/son_moeda.wav')

largura = 640
altura = 640

bg = pygame.image.load('sprites/fundo.png')


x_cobra = int(largura /2)
y_cobra = int(altura /2)

velocidade = 10

x_controle = velocidade
y_controle = 0

x_maca = randint(40,600)
y_maca = randint(50,430)

fonte = pygame.font.SysFont('arial', 30, False, True)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE GAME')

relogio = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 5

morreu = False

def aumenta_combra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 146, 224), (XeY[0],XeY[1],20,20))
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura /2)
    y_cobra = int(altura /2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50,430)
    morreu = False

while True: 
    relogio.tick(30) 
    tela.blit(bg, (0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0

            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
                
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,0,180), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (200,0,0), (x_maca,y_maca,20,20))

    if cobra.colliderect(maca):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        pontos = pontos + 1
        comprimento_inicial +=1
        son_colisao.play()
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', (20), True, True)
        mensagem = 'Game Over! preciona a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, False, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        tela.blit(bg, (0,0))
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)            
            pygame.display.update()
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_combra(lista_cobra)

    tela.blit(texto_formatado, (450,40))
  
    pygame.display.update()