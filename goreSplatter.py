#!usr/bin/env python

import pygame
import random

class GoreSplatter:
    # FUCK YES

    def __init__(self, x, y, dx,dy,impact, hitType, bodyPart):
        self.x = x
        self.y = y
        maxX = abs(int((impact * dx * 10)))
        maxY = abs(int((impact * dy * 10)))
        self.rect = pygame.Rect(x,y,maxX,maxY)
        # where to start from
        originx = originy = 0
        if dx > 0:
            originx = maxX
            #self.x -= maxX
        else:
            originx = 0
            #if (hitType != 1):
            #    self.x += maxX
        if dy > 0:
            originy = 0
            #self.y -= maxY
        else:
            originy = maxY
            #if (hitType != 1):
            #    self.y += maxY 
        midx = int(maxX / 2)
        midy = int(maxY/ 2)
        
        self.screen = pygame.Surface((maxX, maxY))
        self.screen.set_colorkey((255,255,255))
        self.screen.fill((255,255,255))
        if hitType == 1: #explosion
            pygame.draw.circle(self.screen, (0,0,0), (midx,midy), 15, 0)
            self.x += 25 * dx
            self.y += 25 * dy
        if hitType == 2:
            # BONUS
            ndx = random.randint(2,6)
            ndy = random.randint(2,6)
            pygame.draw.line(self.screen, (102,0,0), (originx,originy),
                         (int(originx + impact * ndx),int(originy + impact * ndy)), impact)
            
            pygame.draw.line(self.screen, (102,0,0), (originx,originy),
                (maxX, maxY), impact)

        self.timer = 1500
        if (random.randint(0,100) > 80):            
            rect = bodyPart.get_rect()
            self.screen.blit(bodyPart, (midx,midy))
            self.timer += 1000

        if hitType != 2:
            for i in range(impact):
                x2 = int(midx + random.randint(-4,4) * impact)
                y2 = int(midy + random.randint(-4,4) * impact)
                pygame.draw.circle(self.screen, (102,0,0), (x2, y2), random.randint(5,10), 0)        

    def update(self, dt):
        self.timer -= dt
        return (self.timer < 0)

    def getScreen(self):
        return self.screen

    def getRect(self):
        return self.rect
    def getX(self):
        return self.x
    def getY(self):
        return self.y









        
            
