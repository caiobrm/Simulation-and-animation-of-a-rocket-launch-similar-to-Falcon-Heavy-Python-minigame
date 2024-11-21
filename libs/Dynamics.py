from libs.database import Database
from libs.Rocket import Rocket
from datetime import datetime
timedate = datetime.now()

class dynamics:

    def __init__(self):
        self.ft = 0 ##Força de Empuxo de cada motor
        self.alt = 0.0 ##Altitude
        self.v1 = 0.0 ## Velocidade Final
        self.a = 0.0 ## Aceleração resultante
        self.vr = 0.0 ##Velocidade Final em escala
        self.vry = 0.0
        self.mflow = 0 ##Massa total consumida pelos motores em Kg/s
        self.df = 0.0
        ##Drag (arrasto)
        self.drag = 0.0
        ##Força Peso
        self.p = 0 

dyn = dynamics()

def fthrust(nEngine, enginethrust):
    return nEngine*enginethrust
def masst(mass, massc):
    return mass + massc
def grav(alt):
    g = (Database.G*Database.Mt)/(alt+Database.Rt)**2
    return g

def datm (alt):
    x = alt/5000
    d = ((-0.085*x**3)+(1.675*x**2)+(-10.99*x)+24.6)/20
    return d

def dragforce(v1, alt):
    rocket = Rocket()
    drag = (datm(alt)*rocket.Cx*rocket.Ar*v1**2)/2
    return drag
def pforce(mass, alt):
    Database.g = grav(alt)
    p = mass * Database.g
    return p
def rforce(nEngine, enginethrust, v1, mass, alt):
    if v1 < 0:
        a = (fthrust(nEngine, enginethrust) +dragforce(v1,alt) -pforce(mass,alt))/mass
        return a
    a = (fthrust(nEngine, enginethrust) -dragforce(v1,alt) -pforce(mass,alt))/mass
    return a

def epower(v1):
    intervals = [
        (0, 20, 20),
        (20, 40, 23),
        (40, 70, 24),
        (70, 90, 21),
        (90, 120, 22),
        (120, 160, 20),
        (220, 270, 18),
        (270, 300, 16),
        (300, 310, 16),
        (310, 350, 18),
        (350, 390, 20.5),
        (390, 450, 20),
        (450, 550, 21),
        (550, 650, 20),
        (850, 950, 20),
        (5646, float('inf'), 9),
        (10906, float('inf'), 1)
    ]
    
    for lower, upper, value in intervals:
        if lower < v1 <= upper:
            return value
    
    return 22 #default value