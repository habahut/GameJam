#!usr/bin/env python

from math import sqrt
from pygame import Rect

"""
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

    def getProjectileRate(self, type):
        if (type==1):
            weapon = Bow(0,0,(0,0))
            return weapon.getRate()
        elif (type==2):
            weapon = MachineGun(0,0,(0,0))
            return weapon.getRate()
        elif (type==3):
            weapon = Rocket(0,0,(0,0))
            return weapon.getRate()
        elif (type==4):
            weapon = ShotGun(0,0,(0,0))
            return weapon.getRate()
"""


class Projectile:

    def __init__(self, damage, hitType, rect, speed, impact):
        self.damage = damage
        self.hitType = hitType
        self.rect = rect
        self.speed = speed
        self.dx = 0
        self.dy = 0
        self.impact = impact

    def setTrajectory(self, px,py, mx, my):
        dx = px - mx
        dy = py - my
        d = sqrt(dx * dx + dy * dy)
        self.dx = dx / d * self.speed
        self.dy = dy / d * self.speed

        #print px, py, "    ", mx ,my, "    ", self.dx, self.dy,"    ", self.speed

    def update(self, dt):
        self.rect.centerx -= self.dx * dt
        self.rect.centery -= self.dy * dt

    def getRect(self):
        return self.rect

    def getX(self):
        return self.rect.centerx
    def getY(self):
        return self.rect.centery
    def getDX(self):
        return self.dx
    def getDY(self):
        return self.dy
    def setpos(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y
    def setDxDy(self, dx, dy):
        self.dx = dx
        self.dy = dy
    def getImpact(self):
        return self.impact
    def getDamage(self):
        return self.damage
    def getHitType(self):
        return self.hitType
    

"""
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
"""
