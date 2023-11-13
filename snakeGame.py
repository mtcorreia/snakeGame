# JOGO DA COBRINHA ou SNAKE 'PYTHON' GAME.
# Matheus T. Correia - 10/11/2023

# Arquivo de construção do jogo.

# Imports necessários.
import pygame as pg
import random as r

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Janela do jogo.
pg.init()
pg.display.set_caption("Snake 'Python' Game")
largura, altura = 600, 400
tela = pg.display.set_mode((largura, altura))
tempo = pg.time.Clock()

# Parâmetros da cobra.
tamanho_quadrado = 10
velocidade_jogo = 15

def gerarComida():
    comida_x = round(r.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(r.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)

    return comida_x, comida_y

def desenhoComida(tamanho, comida_x, comida_y):
    pg.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhoCobra(tamanho, pixels):
    for pixel in pixels:
        pg.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhoPontuacao(p):
    pText = pg.font.SysFont("Helvetica", 20)
    text = pText.render(f"Pontos: {p}", False, vermelha)
    tela.blit(text, [1, 1])

def selecionarDirecao(tecla):
    if tecla == pg.K_DOWN:
        direcao_x = 0
        direcao_y = tamanho_quadrado
    elif tecla == pg.K_UP:
        direcao_x = 0
        direcao_y = -tamanho_quadrado
    elif tecla == pg.K_RIGHT:
        direcao_x = tamanho_quadrado
        direcao_y = 0  
    elif tecla == pg.K_LEFT:
        direcao_x = -tamanho_quadrado
        direcao_y = 0

    return direcao_x, direcao_y

# Loop infinito: JOGO
def jogoCobrinha():
    fim = False

    x = largura / 2
    y = altura / 2

    # Cobra começa parada.
    # Velocidade nos eixos X e Y.
    direcao_x = 0
    direcao_y = 0

    tamanho_cobra = 1
    pixels = []

    # Geração da comida da cobra.
    comida_x, comida_y = gerarComida()

    # Looping infinito do jogo.
    while not fim:
        tela.fill(preta)
        
        # Captação das interações do usuário.
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                fim = True
                print("\nFIM DE JOGO!")
            elif evento.type == pg.KEYDOWN:
                direcao_x, direcao_y = selecionarDirecao(evento.key)

        # Desenho da comida a cada tick do jogo.
        desenhoComida(tamanho_quadrado, comida_x, comida_y)

        # Bateu na borda do jogo.
        if x < 0 or x >= largura or y < 0 or y >= altura:
            print("\nBateu em uma das bordas, FIM DE JOGO!")
            fim = True

        # Atualizando o deslocamento da cobra.
        x += direcao_x
        y += direcao_y

        # Desenhando a cobra em cada pixel.
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        # Cobra bate no próprio corpo.
        # Fim de jogo.
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                print("\nBateu em si mesmo, FIM DE JOGO!")
                fim = True

        desenhoCobra(tamanho_quadrado, pixels)
        desenhoPontuacao(tamanho_cobra - 1)

        pg.display.update()

        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerarComida()
            print("+1")

        tempo.tick(velocidade_jogo)

jogoCobrinha()