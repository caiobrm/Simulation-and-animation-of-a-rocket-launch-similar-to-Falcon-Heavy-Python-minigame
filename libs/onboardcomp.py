import pygame
from libs.database import Database
from libs.database import colors
from libs.csvf import *
from datetime import datetime
data_hora = datetime.today()

def text(backgrd, msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, 30)
    texto1 = font.render(msg, True, cor)
    backgrd.blit(texto1,[x, y])

class onboardcomp:
    def __init__(self,backgrd,v1,alt,mass, hour, minute, second):
        ##DISPLAY
        color = colors()
        self.data_hora = datetime.now()
        pygame.draw.rect(backgrd, color.black, [125, 37, 300,125], )
        text(backgrd,Database.str1.format(v1), color.white, 15, Database.large/10, Database.high/10)
        text(backgrd,Database.str2.format(v1*3.6), color.white, 15, Database.large/10, Database.high/15)
        text(backgrd,Database.str3.format(mass), color.white, 15, Database.large/10, Database.high/7.5)
        text(backgrd,Database.str4.format(alt), color.white, 15, Database.large/10, Database.high/6)
        text(backgrd,Database.str5.format(hour, minute, second), color.white, 15, Database.large/10, Database.high/5)
    @csvf
    def log(self, v1, alt, second):

        return v1, alt, second