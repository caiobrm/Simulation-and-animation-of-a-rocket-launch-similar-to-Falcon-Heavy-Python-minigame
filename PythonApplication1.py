import pygame
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
pygame.display.set_caption("Bomberman genérico",)
def game():
    ##
 pos_x = randint(0,(large - size) / 10) * 10
 pos_y = randint(0,(high - size) / 10) * 10
 pos_x2 = randint(0,(large - size) / 10) * 10
 pos_y2 = randint(0,(high - size) / 10) * 10
 speed_x = 0
 speed_y = 0

 dx=0
 dx1=0
 dy = 0
 dy1 = 0

 sair = True
 while sair:
     ##Movements##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            dx=-5
        if event.key == pygame.K_RIGHT:
            dx=+5
        if event.key == pygame.K_UP:
            dy=-5
        if event.key == pygame.K_DOWN:
            dy=+5
        if event.key == pygame.K_a:
            dx1=-5
        if event.key == pygame.K_d:
            dx1=+5
        if event.key == pygame.K_w:
            dy1=-5
        if event.key == pygame.K_s:
            dy1=+5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            dx=0
        if event.key == pygame.K_a:
            dx1=0
        if event.key == pygame.K_RIGHT:
            dx=0
        if event.key == pygame.K_d:
            dx1=0
        if event.key == pygame.K_UP:
            dy=0
        if event.key == pygame.K_w:
            dy1=0
        if event.key == pygame.K_DOWN:
            dy=0
        if event.key == pygame.K_s:
            dy1=0
    
    pos_x= pos_x + dx
    pos_x2= pos_x2 + dx1
    pos_y= pos_y + dy
    pos_y2= pos_y2 + dy1

    backgrd.fill(black)
    pygame.draw.rect(backgrd, white, [pos_x,pos_y,size,size])
    pygame.draw.rect(backgrd, red, [pos_x2,pos_y2,size,size])
    pos_x+=speed_x
    pos_y+=speed_y
    tokei.tick(30)
    if pos_x > large:
        pos_x = 0
    if pos_x < 0:
        pos_x = large - size
    if pos_y >= high:
        pos_y = 0
    if pos_y < 0:
        pos_y = high - size
    if pos_x2 > large:
        pos_x2 = 0
    if pos_x2 < 0:
        pos_x2 = large - size
    if pos_y2 >= high:
        pos_y2 = 0
    if pos_y2 < 0:
        pos_y2 = high - size
    ##
    pygame.display.update()

game()
