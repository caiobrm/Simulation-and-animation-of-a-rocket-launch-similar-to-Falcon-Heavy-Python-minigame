import pygame
from Rocket import Rocket
from Engine import Engine
from database import colors
from database import database
from onboardcomp import onboardcomp
from Dynamics import *
from datetime import datetime
from csvf import *
from datetime import datetime
##########

try:
    pygame.init()
except:
    print("O módulo pygame não foi iniciado corretamente.\n")
##FuncTime
tokei = pygame.time.Clock()
##EndFuncTime
Rocket = Rocket()
data = database()
backgrd = pygame.display.set_mode((data.large,data.high))
data.logo = pygame.Surface.convert_alpha(data.logo)
pygame.display.set_icon(data.logo)
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
 data = database()
 timedate = datetime.now()
 on = onboardcomp(backgrd,dyn.v1,dyn.alt,engine.mass, timedate.hour, timedate.minute, timedate.second)
    ##
 sair = True
 while sair:
     ##Movements##
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE: ## RECOMEÇA
            data.speed_y = 0
            data.pos_y = -384
            data.pos_y2 = -384
            dyn.alt = 0.0
            dyn.v1 = 0.0
            engine.mass = 1338000
            dyn.vry = 0.0
        if event.key == pygame.K_UP: ##ACELERADOR
            engine.nEngine = epower(dyn.v1)
            dyn.v1 = (dyn.v1 + (dyn.a*data.t))
            dyn.vr = dyn.v1/50   
            dyn.alt = dyn.alt + dyn.v1*data.t + ((dyn.a*data.t**2)/2)  
            engine.mass = engine.mass - dyn.mflow*data.t 
            data.speed_y= -dyn.vr
            on.log(dyn.v1,dyn.alt,on.data_hora.second)
            speed_y2 = -dyn.v1
            Rocket.up = True

        if event.key == pygame.K_RIGHT: ##Break
                data.speed_y = 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
             dyn.v1 = dyn.v1 + dyn.a*data.t
             dyn.vr = dyn.v1/50
             engine.nEngine = 0
             dyn.alt = dyn.alt + dyn.v1*data.t + ((dyn.a*data.t**2)/2)  
             data.speed_y = -dyn.vr
             speed_y2 = -dyn.v1
             on.log(dyn.v1,dyn.alt,on.data_hora.second)
        Rocket.up = False

    ##Animations below and above 220m
    if dyn.alt < 220: 
        data.pos_y+= data.speed_y
        data.pos_y2+= speed_y2/100000
        backgrd.blit(bg, (0, -26992))
        if dyn.alt == 0:
            backgrd.blit(data.img1, (data.pos_x, data.pos_y))
        else:
            if Rocket.flycount + 1 >= 90:
                Rocket.flycount = 0
            if (Rocket.up == True):  
                backgrd.blit(data.img[Rocket.flycount//10], (data.pos_x,data.pos_y))
                Rocket.flycount += 1
            if (Rocket.up == False):
                backgrd.blit(data.img1, (data.pos_x, data.pos_y))
    else:
        data.pos_y+= -data.speed_y
        data.pos_y2+= speed_y2/100000
        backgrd.blit(bg, (0, -26992))
        backgrd.blit(bg2, (0, -54672))
        backgrd.blit(bg, (0, data.pos_y - 27352))
        backgrd.blit(bg2, (0, data.pos_y - 55032))
        if dyn.alt > 45000:
            backgrd.fill(color.black)
        if Rocket.flycount + 1 >= 90:
            Rocket.flycount = 0
        if (Rocket.up == True):
            backgrd.blit(data.img[Rocket.flycount//10], (data.pos_x, 360))
            Rocket.flycount += 1
        if (Rocket.up == False):
            backgrd.blit(data.img1, (data.pos_x, 360))
    ##Altimeter
    
    ##ATUALIZAÇÕES## 
    dyn.a = rforce(engine.nEngine,
                   engine.enginethrust, dyn.v1, mass, dyn.alt)
    dyn.mflow = engine.enginec*engine.nEngine
    mass = masst(Rocket.massc, engine.mass)
    timedate = datetime.now()

    if dyn.alt < 0:
        data.pos_y = -384
        data.pos_y2 = -384
        dyn.alt = 0.0
        dyn.v1 = 0.0
        engine.mass = 1338000
        dyn.vry = 0.0

    ##DISPLAY
    on = onboardcomp(backgrd,dyn.v1,dyn.alt,engine.mass, timedate.hour, timedate.minute, timedate.second)
    tokei.tick(data.fps)

    if data.pos_y < 0:
        data.pos_y = data.high - Rocket.size - 23

    pygame.display.update()
    
game()
