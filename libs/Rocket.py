
class Rocket:

    def __init__(self):
        self.white = (255,255,255)
        self.size = 40
        self.massc = 71700 ##Massa de carcaça
        self.Ar = 42.27 ##Área de referência para Arrasto em m^2
        self.Cx = 0.11 ##Coeficiente de arrasto
        self.up = False
        self.flycount = 0
        self.belowalt = True
        self.speed_y = 0
        self.speed_altimeter = 0
        self.pos_x = 635
        self.pos_y = -384
        self.pos_y2 = -384
