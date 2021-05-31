import pygame
from database import database
from database import colors
from csvf import *
from datetime import datetime
data_hora = datetime.today()

def text(backgrd, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 30)
    texto1 = font.render(msg, True, cor)
    backgrd.blit(texto1,[x, y])

class onboardcomp:
    def __init__(self,backgrd,v1,alt,mass, hour, minute, second):
        ##DISPLAY
        data1 = database()
        color = colors()
        self.data_hora = datetime.now()
        pygame.draw.rect(backgrd, color.black, [125, 37, 300,125], )
        text(backgrd,data1.str1.format(v1), color.white, 15, data1.large/10, data1.high/10)
        text(backgrd,data1.str2.format(v1*3.6), color.white, 15, data1.large/10, data1.high/15)
        text(backgrd,data1.str3.format(mass), color.white, 15, data1.large/10, data1.high/7.5)
        text(backgrd,data1.str4.format(alt), color.white, 15, data1.large/10, data1.high/6)
        text(backgrd,data1.str5.format(hour, minute, second), color.white, 15, data1.large/10, data1.high/5)
    @csvf
    def log(self, v1, alt, second):

        return v1, alt, second