#!usr/bin/env python

from projectiles import *
from pygame import Rect

""" hit types:
0 = normal
1 = explodes
2 = piercing
3 = bludgeoning
"""



class Weapon:
    def __init__(self):
        self.rate = 0
        self.timer = 0
        self.damage = 0
        self.hitType = 0

    def shoot(self): pass

class Bow(Weapon):    
    def __init__(self):
        self.rate = 400
        self.timer = 0
        self.damage = 1000
        self.hitType = 2
        self.speed = 4
        self.impact = 30

    def update(self, dt):
        self.timer -= dt

    def shoot(self):
        if self.timer > 0:
            return None
        else:
            self.timer = self.rate
            return Projectile(self.damage, self.hitType, Rect(0,0,30,20), self.speed, self.impact)

class MachineGun(Weapon):
    def __init__(self):
        self.rate = 40
        self.timer = 0
        self.damage = 10
        self.hitType = 0
        self.speed = 3
        self.impact = 8

    def update(self, dt):
        self.timer -= dt

    def shoot(self):
        if self.timer > 0:
            return None
        else:
            self.timer = self.rate
            return Projectile(self.damage, self.hitType, Rect(0,0,7,7), self.speed, self.impact )

class RocketLauncher(Weapon):
    def __init__(self):
        self.rate = 400
        self.timer = 0
        self.damage = 10000
        self.hitType = 1
        self.speed = 2
        self.impact = 50

    def update(self, dt):
        self.timer -= dt

    def shoot(self):
        if self.timer > 0:
            return None
        else:
            self.timer = self.rate
            return Projectile(self.damage, self.hitType, Rect(0,0,32,32), self.speed, self.impact)

class FUCKINGSWORD(Weapon):
    def __init__(self):
        self.rate = 110
        self.timer = 0
        self.damage = 10000
        self.hitType = 3
        self.speed = .01
        self.impact = 40

    def update(self, dt):
        self.timer -= dt

    def shoot(self):
        if self.timer > 0:
            return None
        else:
            self.timer = self.rate
            return Projectile(self.damage, self.hitType, Rect(0,0,32,32), self.speed, self.impact)





        
                
