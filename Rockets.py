import pygame
import math
import numpy
from random import randint
##Colors
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
##endColors
try:
    pygame.init()
except:
    print("O módulo pygame não foi iniciado corretamente.\n")
##Screen
large = 1366   
high = 768
##EndScreen
##SizeChar
size = 10
##EndSizeChar
##FuncTime
tokei = pygame.time.Clock()
##EndFuncTime
backgrd = pygame.display.set_mode((large,high))
pygame.display.set_caption("Rockets",)

def text(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 30)
    texto1 = font.render(msg, True, cor)
    backgrd.blit(texto1,[x, y])

def game():
    ##
 FPS = 60
 pos_x = 683
 pos_y = -384
 speed_y = 0
 mass = 1338500 #Massa de combustível
 masst = (1338500 + 71700) ## Massa total
 g = 9.80665 ## Aceleração Gravitacional
 ft = 0 ##Força de Empuxo de cada motor
 alt = 0.0 ##Altura 
 v2 = 0.0 ## Velocidade Inicial
 v1 = 0.0 ## Velocidade Final
 a = 0.0 ## Aceleração resultante
 t = (1/FPS) ## Unidade de tempo
 vr = 0.0 ##Velocidade Final em escala
 Ar = 42.27 ##Área de referência para Arrasto em m^2
 Cx = 0.11 ##Coeficiente de arrasto
 vy = 0.0
 grav = (g*t)
 nEngine = 0 ## Número de motores
 engine_thrust = 903000 ##Empuxo de cada motor em N
 enginec = 320 ##Consumo de Massa de cada motor em Kg/s
 mflow = 0 ##Massa total consumida pelos motores em Kg/s
 altr = 768 ##Altura em escala.
 str = 'Velocidade : {0:+4.3f} m/s'
 str2 = 'Velocidade : {0:+4.3f} km/h'
 str3 = 'Combustível : {0:4.3f} kg'
 str4 = 'Altura : {0:4.1f} m'
 ##Drag (arrasto)
 drag = 0.0
 ##Força Peso
 p = 0 


 sair = True
 while sair:
     ##Movements##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:##Reabastece
            mass = 1400788
            a = 0
            v1 = 0
            v2 = 0
            vy = 0
            vry = 0
            alt = 0
        if event.key == pygame.K_RIGHT:
             speed_x=0
        if event.key == pygame.K_UP: ##ACELERADOR
                v1 = (v2 + (a*t))##Atualização da Velocidade
                vr = v1/100 #Transformando em Escala
                v2 = v1 #acumulador, visto que no proximo instante v1(final) de agora será a v2(inicial) no próximo
                alt = alt + v1*t + ((a*t**2)/2)##Função horária da altura.
                mass = mass - mflow*t ##Atualização da Massa
                speed_y=-vr
        if event.key == pygame.K_DOWN:
                speed_y= 0
        if event.key == pygame.K_w:
            speed_y=-6
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
           ## v1 = v2 - grav
           ## vry = v1/100
           ## altr = altr + v1*t - ((g*t**2)/2)
            ##speed_y =-vry
            ##v2 = v1
            speed_y = 0
    backgrd.fill(black)
    pygame.draw.circle(backgrd, white, [int(pos_x),int(pos_y)],size)
    pos_y+=speed_y

    ##Determina a força de Empuxo em relação ao número de motores
    nEngine = 22.5
    ft = engine_thrust*nEngine
    
    ##ATUALIZAÇÕES##
    mflow = enginec*nEngine ##Atualiza a massa consumida
    p = masst * g ##Atualiza a força Peso
    drag = (-1*Cx*Ar*v2**2)/2 ##Atualiza a força de arrasto aerodinâmico
    a = (ft + drag -p)/mass ##Atualiza a aceleração resultante

    ##DISPLAY
    text(str.format(v1), white, 15, large/10, high/10)
    text(str2.format(v1*3.6), white, 15, large/10, high/15)
    text(str3.format(mass), white, 15, large/10, high/8)
    text(str4.format(alt), white, 15, large/10, high/6)
    print(altr)

    tokei.tick(FPS)
    if pos_x > large:
        pos_x = 0
    if pos_x < 0:
        pos_x = large - size
    ##if altr <= high:
       ## pos_y = -high
       ## vry = 0
       ## speed_y = 0
        ##altr = 768
        ##v1 = 0
        ##v2 = 0
        ##mass = 1338500
        ##alt = 0
    if pos_y <= 0:
        pos_y = high - size
    ##
    pygame.display.update()

game()