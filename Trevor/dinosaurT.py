#!usr/bin/env python

from math import sqrt

class Dinosaur:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def decide(self, playerX, playerY):
        self.dx = self.x - playerX
        self.dy = self.y - playerY

        d = sqrt(self.dx * self.dx + self.dy * self.dy) 

        self.dx /= d
        self.dy /= d

    def update(self, dt):
        self.x -= self.dx * dt
        self.y -= self.dy * dt

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setDX(self, dx):
        self.dx = dx
    def setDY(self, dy):
        self.dy = dy
