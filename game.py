import pygame
from libs.Rocket import Rocket
from libs.Engine import Engine
from libs.database import colors
from libs.database import Database
from libs.onboardcomp import onboardcomp
from libs.Dynamics import *
from datetime import datetime

try:
    pygame.init()
except:
    print("O módulo pygame não foi iniciado corretamente.\n")
##FuncTime
tokei = pygame.time.Clock()
##EndFuncTime
Rocket = Rocket()
backgrd = pygame.display.set_mode((Database.large,Database.high))
Database.logo = pygame.Surface.convert_alpha(Database.logo)
pygame.display.set_icon(Database.logo)
pygame.display.set_caption("Rocket Dynamics",)

##Image conversion
def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()

bg = loadify('img/bg1.png')
bg2 = loadify('img/bg2.png')
bg3 = loadify('img/bg3.png')
altimeter = loadify('img/altimeter.png')
rocketmeter = loadify('img/rocket.png')
##

def game():
 speed_y2 = 0
    ##
 engine = Engine()
 color = colors()
 mass =  masst(Rocket.massc, engine.mass)
 dyn = dynamics()
 timedate = datetime.now()
 on = onboardcomp(backgrd,dyn.v1,dyn.alt,engine.mass, timedate.hour, timedate.minute, timedate.second)
    ##
 sair = False
 while not sair:
     ##Movements##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP: ##ACELERADOR
            engine.nEngine = epower(dyn.v1)
            dyn.v1 = (dyn.v1 + (dyn.a*Database.t))
            dyn.vr = dyn.v1/50   
            dyn.alt = dyn.alt + dyn.v1*Database.t + ((dyn.a*Database.t**2)/2)  
            engine.mass = engine.mass - dyn.mflow*Database.t 
            Rocket.speed_y= -dyn.vr
            on.log(dyn.v1,dyn.alt,on.data_hora.second)
            speed_y2 = -dyn.v1
            Rocket.up = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
             dyn.v1 = dyn.v1 + dyn.a*Database.t
             dyn.vr = dyn.v1/50
             engine.nEngine = 0
             dyn.alt = dyn.alt + dyn.v1*Database.t + ((dyn.a*Database.t**2)/2)  
             Rocket.speed_y = -dyn.vr
             speed_y2 = -dyn.v1
             on.log(dyn.v1,dyn.alt,on.data_hora.second)
        Rocket.up = False

    ##Animations below and above 220m
    if dyn.alt < 220: 
        Rocket.pos_y+= Rocket.speed_y
        Rocket.pos_y2+= speed_y2/100000
        backgrd.blit(bg, (0, -26992))
        if dyn.alt == 0:
            backgrd.blit(Database.img1, (Rocket.pos_x, Rocket.pos_y))
        else:
            if Rocket.flycount + 1 >= 90:
                Rocket.flycount = 0
            if (Rocket.up == True):  
                backgrd.blit(Database.img[Rocket.flycount//10], (Rocket.pos_x,Rocket.pos_y))
                Rocket.flycount += 1
            if (Rocket.up == False):
                backgrd.blit(Database.img1, (Rocket.pos_x, Rocket.pos_y))
    else:
        Rocket.pos_y+= -Rocket.speed_y
        Rocket.pos_y2+= speed_y2/100000
        backgrd.blit(bg, (0, -26992))
        backgrd.blit(bg2, (0, -54672))
        backgrd.blit(bg, (0, Rocket.pos_y - 27352))
        backgrd.blit(bg2, (0, Rocket.pos_y - 55032))
        if dyn.alt > 45000:
            backgrd.fill(color.black)
        if Rocket.flycount + 1 >= 90:
            Rocket.flycount = 0
        if (Rocket.up == True):
            backgrd.blit(Database.img[Rocket.flycount//10], (Rocket.pos_x, 360))
            Rocket.flycount += 1
        if (Rocket.up == False):
            backgrd.blit(Rocket.img1, (Rocket.pos_x, 360))
    ##Altimeter
    
    ##ATUALIZAÇÕES## 
    dyn.a = rforce(engine.nEngine, engine.enginethrust, dyn.v1, mass, dyn.alt)
    dyn.mflow = engine.enginec*engine.nEngine
    mass = masst(Rocket.massc, engine.mass)
    timedate = datetime.now()

    if dyn.alt < 0:
        Rocket.pos_y = -384
        Rocket.pos_y2 = -384
        dyn.alt = 0.0
        dyn.v1 = 0.0
        engine.mass = 1338000
        dyn.vry = 0.0

    ##DISPLAY
    on = onboardcomp(backgrd,dyn.v1,dyn.alt,engine.mass, timedate.hour, timedate.minute, timedate.second)
    tokei.tick(Database.FPS)

    if Rocket.pos_y < 0:
        Rocket.pos_y = Database.high - Rocket.size - 23

    pygame.display.update()
    
game()
