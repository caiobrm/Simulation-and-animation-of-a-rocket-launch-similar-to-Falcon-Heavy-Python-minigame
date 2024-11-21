import pygame
import math

class Database:
    g = -9.80665  # Aceleração Gravitacional
    FPS = 60
    t = (1 / FPS)
    logo = pygame.image.load('img/Logo1.png')
    speed_y = 0
    speed_altimeter = 0
    pos_x = 635
    pos_y = -384
    pos_y2 = -384
    img = [pygame.image.load(f'img/f{i}.png') for i in range(10)]  # Gerando as imagens dinamicamente
    img1 = pygame.image.load('img/m0.png')
    G = 6.674184 * math.pow(10, -11)
    Mt = 5.972 * math.pow(10, 24)
    Rt = 6371000
    str1 = 'Velocity : {0:+4.3f} m/s'
    str2 = 'Velocity : {0:+4.3f} km/h'
    str3 = 'Fuel : {0:4.2f} kg'
    str4 = 'Height : {0:4.1f} m'
    str5 = 'Horary : ' '{0} : ''{1} : ''{2} s'
    large = 1286  # largura da tela
    high = 688    # altura da tela

class colors:
    white = (255,255,255)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    black = (0,0,0)
    blue1 = (0,182,255)
    background = (1,6,41)
