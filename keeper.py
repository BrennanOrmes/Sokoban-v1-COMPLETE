#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     30/09/2015
# Copyright:   (c) CNYS 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from movingobj import MovingObj

class Keeper(MovingObj):
    #add keeper attributes first!

    def __init__(self, x, r, c):
        """constructor for the warehouse keeper.  Needs to pass in values
       for the character representing the warehouse keeper, the row and the column
       >>>Keeper("$", 2, 3)
       Nonetype"""
        self.char = x
        self.row = r
        self.col = c
        self.diamonds = 0

    def toString(self):
        info = "Keeper " + self.char + " at row " + str(self.row) + " and column " + str(self.col)
        info = info +  " has covered " + str(self.diamonds) + " diamonds today."
        return info

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    #def getDiamonds(self):
        #return self.diamonds

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    """def moveRight(self):
        self.col += 1

    def moveUp(self):
        self.row -=1

    def moveDown(self):
        self.row +=1

    def moveLeft(self):
        self.col -=1"""

    #def eatDiamonds(self):
        #self.diamonds += 1
