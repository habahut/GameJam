#!usr/bin/env python

from math import sqrt
from pygame import Rect

class Dinosaur:

    def __init__(self, x, y):
        self.dx = 0
        self.dy = 0
        self.myrect = Rect(x,y, 30, 44)

    def decide(self, playerX, playerY):
        self.dx = self.myrect.centerx - playerX
        self.dy = self.myrect.centery - playerY

        d = sqrt(self.dx * self.dx + self.dy * self.dy) 
        if d == 0:
            return
        self.dx /= d
        self.dy /= d

    def update(self, dt):
        self.myrect.centerx -= self.dx * dt
        self.myrect.centery -= self.dy * dt

    def getX(self):
        return self.myrect.centerx
    def getY(self):
        return self.myrect.centery
    def getrect(self):
        return self.myrect

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy

