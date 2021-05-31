from database import database
from Rocket import Rocket
from Engine import Engine
from datetime import datetime
from onboardcomp import onboardcomp
rocket = Rocket()
engine = Engine()
data = database()
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
    from database import database
    g = (data.G*data.Mt)/(alt+data.Rt)**2
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
    data.g = grav(alt)
    p = mass * data.g
    return p
def rforce(nEngine, enginethrust, v1, mass, alt):
    if v1 < 0:
        a = (fthrust(nEngine, enginethrust) +dragforce(v1,alt) -pforce(mass,alt))/mass
        return a
    a = (fthrust(nEngine, enginethrust) -dragforce(v1,alt) -pforce(mass,alt))/mass
    return a

def epower (v1):
    if v1>0 and v1 < 20:
        return 20
    if v1 > 20 and v1 < 40:
        return 23
    if v1 > 40 and v1 < 70:
        return 24
    if v1 > 70 and v1 < 90:
        return 21
    if v1 > 90 and v1 < 120:
        return 22
    if v1 > 120 and v1 < 160:
        return 20
    if v1 > 220 and v1 < 270:
        return 18
    if v1 > 270 and v1 < 300:
        return 16
    if v1 > 300 and v1 < 310:
        return 16
    if v1 > 310 and v1 < 350:
        return 18
    if v1 > 350 and v1 < 390:
        return 20.5
    if v1 > 390 and v1 < 450:
        return 20
    if v1 > 450 and v1 < 550:
        return 21
    if v1 > 550 and v1 < 650:
        return 20
    if v1 > 850 and v1 < 950:
        return 20
    if v1 > 5646:
        return 9
    if v1 > 10906:
        return 1
    else:
        return 22
