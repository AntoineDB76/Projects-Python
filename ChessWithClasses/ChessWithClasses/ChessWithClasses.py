import numpy as np
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import pygame
import math

carre=50
pygame.init()
X = 400
Y = 400
display_surface = pygame.display.set_mode((X, Y ))
pygame.display.set_caption('Chess')

@dataclass
class Color:
    COLOR : str

class Chessboard:
    def __init__(self):
        self.chessboard = []
        for i in range(0, 8):
            self.chessboard.append([])
            for j in range(0, 8):
                self.chessboard[i].append(None)

        for i in range(0, 8, 2):
            self.chessboard[0][i] = NoPiece(0, i, Color("black"))
            self.chessboard[1][i] = NoPiece(1, i, Color("white"))
            self.chessboard[2][i] = NoPiece(2, i, Color("black"))
            self.chessboard[3][i] = NoPiece(3, i, Color("white"))
            self.chessboard[4][i] = NoPiece(4, i, Color("black"))
            self.chessboard[5][i] = NoPiece(5, i, Color("white"))
            self.chessboard[6][i] = NoPiece(6, i, Color("black"))
            self.chessboard[7][i] = NoPiece(7, i, Color("white"))
        for i in range(1, 8, 2):
            self.chessboard[1][i] = NoPiece(1, i, Color("black"))
            self.chessboard[2][i] = NoPiece(2, i, Color("white"))
            self.chessboard[3][i] = NoPiece(3, i, Color("black"))
            self.chessboard[4][i] = NoPiece(4, i, Color("white"))
            self.chessboard[5][i] = NoPiece(5, i, Color("black"))
            self.chessboard[6][i] = NoPiece(6, i, Color("white"))
            self.chessboard[7][i] = NoPiece(7, i, Color("black"))
        for i in range(0, 8):
            self.chessboard[1][i] = Pawn(1, i, Color("black"))
            self.chessboard[6][i] = Pawn(6, i, Color("white"))
        self.chessboard[0][3] = Queen(0, 3, Color("black"))
        self.chessboard[7][4] = Queen(7, 4, Color("white"))
        self.chessboard[0][4] = King(0, 4, Color("black"))
        self.chessboard[7][3] = King(7, 3, Color("white"))
        self.chessboard[0][0] = Rook(0, 0, Color("black"))
        self.chessboard[7][0] = Rook(7, 0, Color("white"))
        self.chessboard[0][7] = Rook(0, 7, Color("black"))
        self.chessboard[7][7] = Rook(7, 7, Color("white"))
        self.chessboard[0][1] = Knight(0, 1, Color("black"))
        self.chessboard[7][1] = Knight(7, 1, Color("white"))
        self.chessboard[0][6] = Knight(0, 6, Color("black"))
        self.chessboard[7][6] = Knight(7, 6, Color("white"))
        self.chessboard[0][2] = Bishop(0, 2, Color("black"))
        self.chessboard[7][2] = Bishop(7, 2, Color("white"))
        self.chessboard[0][5] = Bishop(0, 5, Color("black"))
        self.chessboard[7][5] = Bishop(7, 5, Color("white"))
        
        """self.chessboard = np.array([
                       ['B2', 'B3', 'B4', 'B6', 'B5', 'B4', 'B3', 'B2'],
                       ['B1', 'B1' ,'B1', 'B1', 'B1' ,'B1' ,'B1' ,'B1'],
                       ['0', '0', '0', '0', '0', '0', '0', '0'],
                       ['0', '0', '0', '0', '0', '0', '0', '0'],
                       ['0', '0', '0', '0', '0', '0', '0', '0'],
                       ['0', '0', '0', '0', '0', '0', '0', '0'],
                       ['W1', 'W1' ,'W1', 'W1', 'W1' ,'W1' ,'W1' ,'W1'],
                       ['W2', 'W3', 'W4', 'W5', 'W6', 'W4', 'W3', 'W2']])"""

        #self.background = pygame.image.load("background.png")
        self.turn = Color("white")
        self.turnNb = 1
    def nextTurn(self):
        if self.turn == "white":
            self.turn = "black"
            return self.turn
        elif self.turn == "black":
            self.turn = "white"
            return self.turn

    def draw(self):
        return self.chessboard

    #les if correspondent à la move et pas à select
    @staticmethod
    def select(posx, posy):
        #le if et elif inutile ? peut être à supprimer 
        if cb.chessboard[posx][posy].color != None:
            pygame.draw.line(display_surface, "green", (posx*50, posy*50), ((posx)*50, (posy+1)*50), 1)
            pygame.draw.line(display_surface, "green", ((posx+1)*50, posy*50), ((posx+1)*50, (posy+1)*50), 1)
            pygame.draw.line(display_surface, "green", (posx*50, (posy*50)), ((posx+1)*50, (posy)*50), 1)
            pygame.draw.line(display_surface, "green", ((posx)*50, (posy+1)*50), ((posx+1)*50, (posy+1)*50), 1)
       # if cb.chessboard[posx][posy].color == Color("black"):
        #    #cb.chessboard[posx][posy].imageScaledb = pygame.transform.scale(cb.chessboard[posx][posy].imageb, (53, 53))
         #   pygame.draw.line(display_surface, "green", (posx*50, posy*50), ((posx)*50, (posy+1)*50), 1)
          #  pygame.draw.line(display_surface, "green", ((posx+1)*50, posy*50), ((posx+1)*50, (posy+1)*50), 1)
            #pygame.draw.line(display_surface, "green", (posx*50, (posy*50)), ((posx+1)*50, (posy)*50), 1)
            #pygame.draw.line(display_surface, "green", ((posx)*50, (posy+1)*50), ((posx+1)*50, (posy+1)*50), 1)
        #elif cb.chessboard[posx][posy].color == Color("white"):
            #cb.chessboard[posx][posy].imageScaledw = pygame.transform.scale(cb.chessboard[posx][posy].imageb, (53, 53))
         #   pygame.draw.line(display_surface, "green", (posx*50, posy*50), ((posx)*50, (posy+1)*50), 1)
          #  pygame.draw.line(display_surface, "green", ((posx+1)*50, posy*50), ((posx+1)*50, (posy+1)*50), 1)
           # pygame.draw.line(display_surface, "green", (posx*50, (posy*50)), ((posx+1)*50, (posy)*50), 1)
            #pygame.draw.line(display_surface, "green", ((posx)*50, (posy+1)*50), ((posx+1)*50, (posy+1)*50), 1)
    
    #à travailler
    def selectAttack(posx, posy):
        return 0


class ChessPiece():
    def __init__(self, color, posx, posy):
        self.color = color
        self.alive = True
        self.posx = posx
        self.posy = posy

class NoPiece(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imagew = pygame.image.load("yellowsquare.png")
        self.imageb = pygame.image.load("brownsquare.png")
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY

class Pawn(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("pawnb.png")
        self.imagew = pygame.image.load("pawnw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY

        self.possibleMoves = []

    def moveOrAttack(posx, posy):
        if self.color == "white":
            #il faut rajouter si la case en question existe vraiment
            if cb.chessboard[posx][posy-1] == None:
                self.possibleMoves.append([0,-1])
                if cb.chessboard[posx][posy-2] == None:
                    self.possibleMoves.append([0,-2])
            if cb.chessboard[posx-1][posy-1] != None and cb.chessboard[posx-1][posy-1].color != self.color:
                self.possibleMoves.append([-1,-1])
            if cb.chessboard[posx+1][posy-1] != None and cb.chessboard[posx+1][posy-1].color != self.color:
                self.possibleMoves.append([1,-1])
            for move in self.possibleMoves:
                print("possibleMoves : "+ self.possibleMoves)
                Chessboard.select(move[0], move[1])

class Queen(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("queenb.png")
        self.imagew = pygame.image.load("queenw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY
class King(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("kingb.png")
        self.imagew = pygame.image.load("kingw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY
class Rook(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("rookb.png")
        self.imagew = pygame.image.load("rookw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY
class Knight(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("knightb.png")
        self.imagew = pygame.image.load("knightw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY
class Bishop(ChessPiece):
    def __init__(self, posX, posY, color):
        super().__init__(posX, posY, color)
        self.color = color
        self.imageb = pygame.image.load("bishopb.png")
        self.imagew = pygame.image.load("bishopw.png")
        self.imageScaledb = pygame.transform.scale(self.imageb, (50, 50))
        self.imageScaledw = pygame.transform.scale(self.imagew, (50, 50))
        self.hasMoved = False
        self.posX = posX
        self.posY = posY
    #if chessboard[posy+1][posx+1] == 'B' or chessboard[posy+1][posx-1] == 

    #def moveAhead(self, stepPos=[]):
       #if turnNb == 1 or turnNb == 2:
       #if chessboard[posy][posx] == 'W1':
            #chessboard[posy][posx] = '0'
            #chessboard[posy-1][posx]
        #if chessboard[posy][posx] == 'B1':
         #   chessboard[posy][posx] = '0'
          #  chessboard[posy+1][posx]
        #return 0
       
cb = Chessboard()
cb.draw()
i = 0       
pieces = []
while True:
    for i in cb.chessboard:
        for j in range(0,8):
            if i[j] != None:
                if i[j].color == Color('black'):
                    display_surface.blit(i[j].imageScaledb, (i[j].posY*50, i[j].posX*50))
                    print(i[j].color)
                elif i[j].color == Color('white'):
                    display_surface.blit(i[j].imageScaledw, (i[j].posY*50, i[j].posX*50))
                    print(i[j].color)
#    display_surface.blit(cb.background, (1000,1000))
  
    for event in pygame.event.get() :
        #selection
        if event.type == pygame.MOUSEBUTTONUP:
            (posx, posy) = pygame.mouse.get_pos()
            pieceposx = posx/carre
            pieceposxrounded = math.ceil(pieceposx)
            print(pieceposxrounded)
            pieceposy = posy/carre
            pieceposyrounded = math.ceil(pieceposy)
            print(pieceposyrounded)
            Chessboard.select(pieceposxrounded-1, pieceposyrounded-1)
            
            if cb.chessboard[pieceposxrounded-1][pieceposyrounded-1].color == cb.turn:
                print(cb.chessboard[pieceposxrounded-1][pieceposyrounded-1].color)
                cb.chessboard[pieceposxrounded-1][pieceposyrounded-1].moveOrAttack(pieceposxrounded-1, pieceposyrounded-1)
                #Chessboard.selectAttack()

            cb.chessboard[1][0] = None
            cb.chessboard[1][0] = NoPiece(1,0, Color("white"))
            cb.chessboard[3][0] = Pawn(3,0,Color("black"))
        #if event.type == pygame.MOUSEBUTTONUP:
            #cb.chessboard[1][0] = None
            #cb.chessboard[1][0] = NoPiece(1,0, Color("white"))
            #cb.chessboard[3][0] = Pawn(3,0,Color("black"))
            #Chessboard.select(3, 0)
        if event.type == pygame.QUIT :
            pygame.quit()
        pygame.display.update() 


#for i in cb.chessboard:
#    if i[0] == 'B':
#        print(i[0])


