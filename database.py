import pygame
import math
class database:
    def __init__(self):
        self.g = -9.80665 ## Aceleração Gravitacional
        FPS = 60
        self.fps = 60
        self.t = (1/FPS)
        self.logo = pygame.image.load('img/Logo1.png')
        self.speed_y = 0
        self.speed_altimeter = 0
        self.pos_x = 635
        self.pos_y = -384
        self.pos_y2 = -384
        self.img = [pygame.image.load('img/f0.png'), pygame.image.load('img/f1.png'), pygame.image.load('img/f2.png'), pygame.image.load('img/f3.png'), pygame.image.load('img/f4.png'), pygame.image.load('img/f5.png'), pygame.image.load('img/f6.png'), pygame.image.load('img/f7.png'), pygame.image.load('img/f8.png'), pygame.image.load('img/f9.png')]
        self.img1 = pygame.image.load('img/m0.png')
        self.G = 6.674184*math.pow(10,-11)
        self.Mt = 5.972*math.pow(10,24)
        self.Rt = 6371000
        self.str1 = 'Velocity : {0:+4.3f} m/s'
        self.str2 = 'Velocity : {0:+4.3f} km/h'
        self.str3 = 'Fuel : {0:4.2f} kg'
        self.str4 = 'Height : {0:4.1f} m'
        self.str5 = 'Horary : ' '{0} : ''{1} : ''{2} s'
        ##Screen
        self.large = 1286   
        self.high = 688

class colors:
    def __init__(self):
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.black = (0,0,0)
        self.blue1 = (0,182,255)
        self.background = (1,6,41)
