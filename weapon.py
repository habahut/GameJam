from math import sqrt

class WeaponFactory:
    def createProjectile(self, PlayerX, PlayerY, mouse, type):
        if (type==1):
            return Bow(PlayerX, PlayerY, mouse)
        elif (type==2):
            return MachineGun(PlayerX, PlayerY, mouse)
        elif (type==3):
            return Rocket(PlayerX, PlayerY, mouse)
        elif (type==4):
            return ShotGun(PlayerX, PlayerY, mouse)

class Weapon:

    def __init__(self, PlayerX, PlayerY, mouse, type):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

        self.rate = 0
        self.power = 0
        self.explode = 0

    def update(self, dt):
        self.x -= self.dx * dt * self.rate
        self.y -= self.dy * dt * self.rate

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy

class Bow(Weapon):

    def __init__(self, PlayerX, PlayerY, mouse):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

        self.rate = 0.4
        self.power = 6
        self.explode = 0

class MachineGun(Weapon):

    def __init__(self, PlayerX, PlayerY, mouse):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

        self.rate = 1
        self.power = 2
        self.explode = 0

class Rocket(Weapon):

    def __init__(self, PlayerX, PlayerY, mouse):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

        self.rate = 0.2
        self.power = 10
        self.explode = 1

class ShotGun(Weapon):

    def __init__(self, PlayerX, PlayerY, mouse):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

        self.rate = 0.5
        self.power = 3
        self.explode = 0