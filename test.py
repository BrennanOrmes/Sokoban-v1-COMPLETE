#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brennan
#
# Created:     03/11/2015
# Copyright:   (c) CNYS 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#class imports
from maze import Maze
from keeper import Keeper
from crate import Crate

#add in the pygame imports
import random, sys, copy, os, pygame
from pygame.locals import *

score = 0
moves = 0
maze = Maze()
keeper = Keeper("^", 4, 1)
crate1 = Crate("/", 4, 2)
maze.placeCrate("/", 4, 2)



FPS = 30                    # frames per second to update the screen
WINWIDTH = 800              # width of the program's window, in pixels
WINHEIGHT = 600             # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2) #you need to know 1/2 sizes so you can
HALF_WINHEIGHT = int(WINHEIGHT / 2) #place things centrally

# The total width and height of each tile in pixels.
TILEWIDTH = 32
TILEHEIGHT = 32
TILEFLOORHEIGHT = 32

BRIGHTBLUE = (  0, 170, 255)
WHITE      = (255, 255, 255)
BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

#A dictionary of the images used.  You can then use#floor, wall etc
#in place of the whole pathname

IMAGESDICT = {'floor': pygame.image.load("Images/floor.gif"),
              'wall': pygame.image.load("Images/wall.gif"),
              'diamond': pygame.image.load("Images/diamond.gif"),
              'keeper': pygame.image.load("Images/keeper.gif"),
              'crate': pygame.image.load("Images/crate.gif") }

TILEMAPPING = { '#':IMAGESDICT['wall'],
                ' ':IMAGESDICT['floor'],
                '@':IMAGESDICT['diamond'],
                '/':IMAGESDICT['crate'],
                '^':IMAGESDICT['keeper']}

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Keeper Maze v 7.00 Moves: '+str(moves))
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

def moveKeeperLeft():
    global score
    #mvoving the keeper to the left...
    #BEFORE you move the keeper, check he can move!
    x = maze.getCharAtPos(keeper.getRow(), keeper.getCol()-1)
    #Wall Check for crates
    y = maze.getCharAtPos(keeper.getRow(), keeper.getCol()-2)
    if x == "#":
        print "This is a wall!"
    elif x == "/":
        if y == "#":
            print "This is a wall!"
        elif y == "@":
            print "You have covered all diamonds!"
            score = score + 1
            NextLevel()

        else:
            maze.clearAtPos(crate1.getRow(), crate1.getCol())
            crate1.moveLeft()
            maze.placeCrate("/", crate1.getRow(), crate1.getCol())
    else:
        #If it is not a wall, what if it is a diamond?
        if x == "@":
            print "You cant move onto diamonds"
        else:
            maze.clearAtPos(keeper.getRow(), keeper.getCol())
            keeper.moveLeft()
            maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())

    print maze.toString()
    print keeper.toString()




def moveKeeperRight():
    global score
    #moving the keeper to the right....
    #BEFORE you move the keeper, check he CAN move!
    x = maze.getCharAtPos(keeper.getRow(), keeper.getCol()+1)
    #Wall Check for crates
    y = maze.getCharAtPos(keeper.getRow(), keeper.getCol()+2)
    if x == "#":
        print "This is a wall!"
    elif x == "/":
        if y == "#":
            print "This is a wall!"
        elif y == "@":
            print "You have covered all diamonds!"
            score = score + 1
            NextLevel()
        else:
            maze.clearAtPos(crate1.getRow(), crate1.getCol())
            crate1.moveRight()
            maze.placeCrate("/", crate1.getRow(), crate1.getCol())
    else:
       #If it is not a wall, what if it is a diamond?
        if x == "@":
            print "You cant move onto diamonds"
        else:
            maze.clearAtPos(keeper.getRow(), keeper.getCol())
            keeper.moveRight()
            maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())

    print maze.toString()
    print keeper.toString()

#define functions for moveKeeperUp() moveKeeperDown() moveKeeperLeft()

def moveKeeperUp():
    global score
    #moving the keeper up
    #BEFORE you move the keeper, check he CAN move!
    x = maze.getCharAtPos(keeper.getRow()-1, keeper.getCol())
    #Wall Check for crates
    y = maze.getCharAtPos(keeper.getRow()-2, keeper.getCol())
    if x == "#":
        print "This is a wall!"
    elif x == "/":
        if y == "#":
            print "This is a wall!"
        elif y == "@":
            print "You have covered all diamonds!"
            score = score + 1
            NextLevel()
        else:
            maze.clearAtPos(crate1.getRow(), crate1.getCol())
            crate1.moveUp()
            maze.placeCrate("/", crate1.getRow(), crate1.getCol())
    else:
        #If it is not a wall, what if it is a diamond?
        if x == "@":
            print "You cant move onto diamonds"
        else:
            maze.clearAtPos(keeper.getRow(), keeper.getCol())
            keeper.moveUp()
            maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
    print maze.toString()
    print keeper.toString()

def moveKeeperDown():
    global score
    #moving the keeper down
    #BEFORE you move the keeper, check he CAN move!
    x = maze.getCharAtPos(keeper.getRow()+1, keeper.getCol())
    #Wall Check for crates
    y = maze.getCharAtPos(keeper.getRow()+2, keeper.getCol())
    if x == "#":
        print "This is a wall!"
    elif x == "/":
        if y == "#":
            print "This is a wall!"
        elif y == "@":
            print "You have covered all diamonds!"
            score = score + 1
            NextLevel()
        else:
            maze.clearAtPos(crate1.getRow(), crate1.getCol())
            crate1.moveDown()
            maze.placeCrate("/", crate1.getRow(), crate1.getCol())
    else:
       #If it is not a wall, what if it is a diamond?
        if x == "@":
            print "You cant move onto diamonds"
        else:
            maze.clearAtPos(keeper.getRow(), keeper.getCol())
            keeper.moveDown()
            maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
    print maze.toString()
    print keeper.toString()

def main():
    global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, BASICFONT, moves
    maze.placeKeeper('^', 4,1)
    print maze.toString()
    drawMap(maze)
    while True:

        #thread 1 - look for an action
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moveKeeperRight()
                    moves = moves + 1
                    pygame.display.set_caption('Keeper Maze v 7.00 Moves: '+str(moves))
                elif event.key == K_UP:
                    moveKeeperUp()
                    moves = moves + 1
                    pygame.display.set_caption('Keeper Maze v 7.00 Moves: '+str(moves))
                elif event.key == K_SPACE:
                    restart()
                elif event.key == K_DOWN:
                    moveKeeperDown()
                    moves = moves + 1
                    pygame.display.set_caption('Keeper Maze v 7.00 Moves: '+str(moves))
                elif event.key == K_LEFT:
                    moveKeeperLeft()
                    moves = moves + 1
                    pygame.display.set_caption('Keeper Maze v 7.00 Moves: '+str(moves))
                else:
                    pass
            mapNeedsRedraw = True

        #thread 2: redraw the screen
        DISPLAYSURF.fill(BGCOLOR) #draws the turquoise background
        #if something has changed, redraw....
        if mapNeedsRedraw:
            mapSurf = drawMap(maze)
            mapNeedsRedraw = False

        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        # Draw the map on the DISPLAYSURF object.
        DISPLAYSURF.blit(mapSurf, mapSurfRect)

        pygame.display.update() # draw DISPLAYSURF to the screen.
        FPSCLOCK.tick()

def drawMap(maze):
    #draw the tile sprites onto this surface.
    #this creates the visual map!
    mapSurfWidth = maze.getWidth() * TILEWIDTH
    mapSurfHeight = maze.getHeight() * TILEHEIGHT
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR)
    for h in range(maze.getHeight()):
        for w in range(maze.getWidth()):
            thisTile = pygame.Rect((w * TILEWIDTH, h * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
            if maze.getCharAtPos(h, w) in TILEMAPPING:
                #checks in the TILEMAPPING directory above to see if there is a
                #matching picture, then renders it
                baseTile = TILEMAPPING[maze.getCharAtPos(h,w)]

            # Draw the tiles for the map.
            mapSurf.blit(baseTile, thisTile)
    return mapSurf

def restart():
    """This function is made to determin what level will be reset.
    When the player covers the diamond, the score goes up.
    Once a level is finished, this function is called and it will point to what level will be next"""
    if score == 0:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.__init__()

    if score == 1:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel2()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 2:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel3()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 3:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel4()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 4:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel5()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)



def terminate():
    #shutdown routine
    pygame.quit()
    sys.exit()

def NextLevel():
    """This function is made to determin what level will be next.
    When the player covers the diamond, the score goes up.
    Once a level is finished, this function is called and it will point to what level will be next"""
    if score == 1:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel2()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 2:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel3()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 3:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel4()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)
    elif score == 4:
        maze.clearAtPos(keeper.getRow(), keeper.getCol())
        keeper.setRow(4)
        keeper.setCol(1)
        crate1.setRow(4)
        crate1.setCol(2)
        maze.goToLevel5()

        maze.placeKeeper(keeper.getChar(), keeper.getRow(), keeper.getCol())
        maze.placeCrate(crate1.getChar(), crate1.getRow(), crate1.getCol())
        drawMap(maze)

    else:
        #error trap incase it goes beyond the max levels
        print "game over!"
        pygame.quit()
        sys.exit()



if __name__ == '__main__':
    main()
