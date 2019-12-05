from Cell import *
import random
import time
import csv
from numpy import array
from PIL import Image

MOORE_NEIGHBOURHOOD = [(-1,-1), (0,-1),  (+1,-1),
                       (-1,0),(0,0),  (+1,0),
                       (-1,+1), (0,+1),  (+1,+1)]

VONNEUMANN_NEIGHBOURHOOD = [(0, -1),
                             (-1, 0),(0,0), (+1, 0),
                             (0, +1)]
HEXAGONAL_LEFT = [(-1,-1), (-1,0), (0,-1),(0,0), (0,1),(1,0),(1,1)]
HEXAGONAL_RIGHT = [(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0)]
PENTAGONAL_LEFT = [(-1,-1), (0,-1),
                       (-1,0),(0,0),
                       (-1,+1), (0,+1)]
PENTAGONAL_RIGHT = [ (0,-1),  (+1,-1),
                    (0,0),  (+1,0),
                     (0,+1),  (+1,+1)]

colour_rule = {
    # Syntax is - cell value: (R, G, B)
    0: (255, 255, 255)
    }

def generateColorRule(nrOfColours):
    for key in range(1,nrOfColours+1):
        colour_rule[key]=(random.randrange(0,255,1,int),random.randrange(0,255,1,int),random.randrange(0,255,1,int))


class Board(Cell):
    def __init__(self,dimX,dimY,nrOfSeeds,neighborhood):
        self.dimX=dimX
        self.dimY=dimY
        self.board=[[]]
        self.generate()
        self.generateSeeds(nrOfSeeds)
        self.neighborhood=neighborhood
        self.boarder=False


    def getCell(self,row,col):
        return self.board[row][col]

    def setCell(self,row,col,ID,nextID,colour):
        self.board[row][col]=Cell(row,col,ID,nextID,colour)

    def setCellNextState(self,row,col,ID):
        self.board[row][col].setNextID(ID)
        self.board[row][col].setColour(colour_rule[ID])

    def generate(self):
        self.board=[[Cell(i,j,0,0,colour_rule[0]) for i in range(0,self.dimX)] for j in range(0,self.dimY)]


    def generateSeeds(self,nrOfSeeds):
        generateColorRule(nrOfSeeds)
        for s in range(1,nrOfSeeds+1):
            row=random.randrange(0,self.dimX,1,int)
            col=random.randrange(0,self.dimY,1,int)
            ID=s
            colour=colour_rule[ID]
            self.setCell(row,col,ID,ID,colour)


    def iteration(self):
        empty_cell=0
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                if(self.getCell(i,j).getID()):
                    self.evolveCell(i,j)
                else:
                    empty_cell+=1
        self.updateBoard()
        return empty_cell

    def updateBoard(self):
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                self.board[i][j].update()
        self.saveImage()


    def getNeighbors(self,row,col):
        IDList = []
        for rule in self.neighborhood:
            nei_row = (row + rule[0])
            nei_col = (col + rule[1])

            if self.boarder is True:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    IDList.append(0)
                    continue
            else:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    nei_row = nei_row % self.dimX
                    nei_col = nei_col % self.dimY

            IDList.append(self.board[nei_row][nei_col].ID)

        ID = self.calculateID(IDList,self.getCell(row,col).getID())
        return ID

    def setNeighbors(self,row,col,ID):
        for rule in self.neighborhood:
            nei_row = (row + rule[0])
            nei_col = (col + rule[1])

            if self.boarder is True:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                   continue
            else:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    nei_row = nei_row % self.dimX
                    nei_col = nei_col % self.dimY

            if(self.getCell(nei_row,nei_col).getID()==0):
                self.setCellNextState(nei_row,nei_col,ID)

    def calculateID(self,IDList,cellID):
        NO_CELL = 0
        set_id = 0
        most_frequent = 0
        unique_vals = set(IDList)
        if len(IDList) > 0:
            for val in unique_vals:
                if val != NO_CELL:
                    frequence = IDList.count(val)
                    if frequence == most_frequent:
                        set_id = cellID
                    elif frequence > most_frequent:
                        most_frequent = frequence
                        set_id = val
        return set_id

    def evolveCell(self,row,col):
        ID=self.getNeighbors(row,col)
        self.setNeighbors(row,col,ID)

    def intBoard(self):
        intBoard = array([[self.board[i][j].colour for i in range(0, self.dimX)] for j in range(0, self.dimY)])
        return intBoard

    def intBoardID(self):
        intBoard = array([[self.board[i][j].ID for i in range(0, self.dimX)] for j in range(0, self.dimY)])
        return intBoard

    def saveImage(self):
        img = Image.new('RGB', (self.dimX, self.dimX))
        pixels = img.load()

        for j in range(0, self.dimX):
            for i in range(0, self.dimY):
                pixels[i, j] = colour_rule[self.board[i][j].getID()]
        img.save('CA_img.png')
        return img

    def writeToCSV(self):
        with open("shot.csv", "a") as my_csv:
            my_csv.seek(0)
            csvWriter = csv.writer(my_csv, delimiter=',')
            arr=self.intBoardID()
            csvWriter.writerows(arr)
