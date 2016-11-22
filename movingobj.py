#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     06/01/2016
# Copyright:   (c) Brennan 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class MovingObj:
    def __init__(self, x, r, c):
        """constructor for the warehouse keeper.  Needs to pass in values
       for the character representing the warehouse keeper, the row and the column
       >>>Keeper("$", 2, 3)
       Nonetype"""
        self.char = x
        self.row = r
        self.col = c
        self.diamonds = 0


    def moveRight(self):
        self.col += 1

    def moveUp(self):
        self.row -=1

    def moveDown(self):
        self.row +=1

    def moveLeft(self):
        self.col -=1
