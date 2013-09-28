from math import sqrt

class Weapon:

    def __init__(self, bulletspeed, rateoffire, bulletdamage):
        self.bulletspeed = bulletspeed
        self.rateoffire = rateoffire
        self.bulletdamage = bulletdamage

        self.currentdelay = 0

    def shoot(self, dt):
        if (self.currentdelay > 0):
            return None
        else:

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy
