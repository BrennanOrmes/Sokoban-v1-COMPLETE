#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     17/11/2015
# Copyright:   (c) Brennan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from movingobj import MovingObj
class Crate(MovingObj):

    def __init__(self, x, r, c):
        self.char = x
        self.row = r
        self.col = c

    def toString(self):
        info = "The crates's position is (" + str(self.row) + "," + str(self.col) + ")"
        return info

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    """def moveRight(self):
        self.col += 1

    def moveLeft(self):
        self.col -= 1

    def moveUp(self):
        self.row -= 1

    def moveDown(self):
        self.row += 1"""
