import pygame
class Block:
    def __init__(self,x,y,barva,okno,velikost):
        self.x = x
        self.y = y
        self.barva = barva
        self.okno = okno
        self.velikost = velikost
        self.cords = [self.x, self.y]
    def vykresli(self):
        pygame.draw.rect(self.okno, self.barva, (self.x, self.y, self.velikost, self.velikost))
    def kolize(self,pozice_hada):
        if pozice_hada[0] == self.cords:
            return True
        else:
            return False