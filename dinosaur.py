#!usr/bin/env python

from math import sqrt
from pygame import Rect
import random

class Dinosaur:

    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.myrect = Rect(x,y, 59, 88)
        self.invi_timer = 500
        self.jump_timer = 500
        self.shield_timer = 500

    def decide(self, playerX, playerY):
        self.dx = self.myrect.centerx - playerX
        self.dy = self.myrect.centery - playerY

        d = sqrt(self.dx * self.dx + self.dy * self.dy) 
        if d == 0:
            return
        self.dx /= d * 2
        self.dy /= d * 2
        
    def update(self, dt):
        self.myrect.centerx -= self.dx * dt
        self.myrect.centery -= self.dy * dt

    def getX(self):
        return self.myrect.centerx
    def getY(self):
        return self.myrect.centery
    def getRect(self):
        return self.myrect
    def getInviTimer(self):
        return self.invi_timer
    def getShieldTimer(self):
        return self.shield_timer

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy

class Shield_Dino(Dinosaur):

    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.myrect = Rect(x,y, 59, 88)
        self.invi_timer = 500
        self.jump_timer = 300
        self.shield_timer = 500

    def update(self, dt):
        self.myrect.centerx -= self.dx * dt
        self.myrect.centery -= self.dy * dt
        if self.shield_timer > 0:
            self.shield_timer -= dt
        else:
            self.shield_timer = 500

class Invi_Dino(Dinosaur):

    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.myrect = Rect(x,y, 59, 88)
        self.invi_timer = 500
        self.jump_timer = 300
        self.shield_timer = 100

    def update(self, dt):
        self.myrect.centerx -= self.dx * dt
        self.myrect.centery -= self.dy * dt
        if self.invi_timer > 0:
            self.invi_timer -= dt
        else:
            self.invi_timer = 500

class Jump_Dino(Dinosaur):
    
    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.myrect = Rect(x,y, 59, 88)
        self.invi_timer = 500    
        self.jump_timer = 300
        self.shield_timer = 500

    def update(self, dt):
        if self.jump_timer > 0:
            self.jump_timer -= dt
            self.myrect.centerx -= self.dx * dt
            self.myrect.centery -= self.dy * dt
        else:
            self.jump_timer = random.uniform(2,5) * 100
            self.myrect.centerx -= self.dx * dt * 50
            self.myrect.centery -= self.dy * dt * 50
