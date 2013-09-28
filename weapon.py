from math import sqrt

class Weapon:

    def __init__(self, PlayerX, PlayerY, mouse):
        self.x = PlayerX
        self.y = PlayerY
        self.dx = self.x - mouse[0]
        self.dy = self.y - mouse[1]
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
