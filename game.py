import pygame
import math
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
large = 800
high = 600
##EndScreen
##SizeChar
size = 30
##EndSizeChar
##FuncTime
tokei = pygame.time.Clock()
##EndFuncTime
backgrd = pygame.display.set_mode((large,high))
pygame.display.set_caption("Rockets",)

def game():
    ##
 highrocket = 70
 speed_x = 0
 pos_x = 600
 pos_y = 400
 speed_y = 0
 distance = pos_x - highrocket
 massr = 27900
 massp = 544600-massr
 mass = 544600
 ##Drag (arrasto)
 drag = -math.ceil(0.04*1.23*3.848451001*1.2922*6)
 ##Gravitational force
 gf = (6.674184*math.pow(10,-11)*5.9736*math.pow(10,24)*mass)/math.pow(distance*6371000,2)

 sair = True
 while sair:
     ##Movements##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed_x=-6
        if event.key == pygame.K_RIGHT:
            speed_x=+6
        if event.key == pygame.K_UP:
            speed_y= -6 - drag
        if event.key == pygame.K_DOWN:
            speed_y=+6
        if event.key == pygame.K_w:
            speed_y=-6
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            speed_x=0
        if event.key == pygame.K_RIGHT:
            speed_x=0
        if event.key == pygame.K_UP:
            speed_y=0
        if event.key == pygame.K_DOWN:
            speed_y=0
        if event.key == pygame.K_w:
            speed_y=0
    backgrd.fill(black)
    pygame.draw.rect(backgrd, white, [pos_x,pos_y,size,size])
    pos_x+=speed_x
    pos_y+=speed_y
    tokei.tick(60)
    if pos_x > large:
        pos_x = 0
    if pos_x < 0:
        pos_x = large - size
    if pos_y >= high:
        pos_y = 0
    if pos_y < 0:
        pos_y = high - size
    ##
    pygame.display.update()

game()