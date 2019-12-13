from Cell import *
import math
from csv import reader,writer,excel
from numpy import array, loadtxt
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Curvature import *

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
    0: (255, 255, 255),
    1: (0,0,0)
    }

def generateColorRule(nrOfColours):
    for key in range(2,nrOfColours+2):
        colour_rule[key]=(random.randrange(0,255,1,int),random.randrange(0,255,1,int),random.randrange(0,255,1,int))


class Board(Cell):
    def __init__(self,dimX,dimY,nrOfSeeds,neighborhood, border, radius,nrOfInclusions):
        self.dimX=dimX
        self.dimY=dimY
        self.board=[[]]
        self.neighborhood=neighborhood
        self.border=border
        self.minR=radius[0]
        self.maxR=radius[1]
        self.nrOfInclusions=nrOfInclusions
        self.curvature=False
        self.probability=100
        self.generate()
        self.generateSeeds(nrOfSeeds)
        if(self.nrOfInclusions>0):
            if(radius[0]!=0 and radius[1]!=0):
                self.generateInclusions()


    def getCell(self,row,col):
        return self.board[row][col]

    def setCell(self,row,col,ID,nextID,colour):
        self.board[row][col]=Cell(row,col,ID,nextID,colour)

    def setCurvature(self,curvature,probability):
        self.curvature=curvature
        self.probability=probability


    def setCellNextState(self,row,col,ID):
        self.board[row][col].setNextID(ID)
        self.board[row][col].setColour(colour_rule[ID])

    def generate(self):
        self.board=[[Cell(i,j,0,0,colour_rule[0]) for j in range(0,self.dimY)] for i in range(0,self.dimX)]

    def generateInclusions(self):
        for inclusion in range(0,self.nrOfInclusions):
            r = random.randrange(self.minR,self.maxR,1,int)
            cx = random.randrange(0, self.dimX, 1, int)
            cy = random.randrange(0, self.dimY, 1, int)
            for x in range(cx - r, (cx + r)+1):
                for y in range(cy - r, (cy + r)+1):
                    if x < 0 or x >= self.dimX or y < 0 or y >= self.dimY:
                        x = x % self.dimX
                        y = y % self.dimY
                    if math.sqrt((cx - x) ** 2 + (cy - y) ** 2) <= r:
                        self.setCell(x,y,1,1,colour_rule[1])


    def generateSeeds(self,nrOfSeeds):
        generateColorRule(nrOfSeeds)
        for s in range(2,nrOfSeeds+2):
            row=random.randrange(0,self.dimX,1,int)
            col=random.randrange(0,self.dimY,1,int)
            ID=s
            colour=colour_rule[ID]
            if(self.getCell(row,col).ID==0):
                self.setCell(row,col,ID,ID,colour)


    def iteration(self):
        empty_cell=0
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                if(self.getCell(i,j).getID() and self.getCell(i,j).getID()!=1):
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

            if self.border is True:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    IDList.append(0)
                    continue
            else:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    nei_row = nei_row % self.dimX
                    nei_col = nei_col % self.dimY

            # if(self.board[nei_row][nei_col].ID!=1):
            IDList.append(self.board[nei_row][nei_col].ID)

        if(self.curvature==True):
            if(Rule1(IDList)):
                ID=self.board[row][col].ID
                print("RULE 1")
            elif(Rule2(IDList)):
                ID=self.board[row][col].ID
                print("RULE 2")
            elif(Rule3(IDList)):
                ID=self.board[row][col].ID
                print("RULE 3")
            elif(Rule4(IDList,self.probability)):
                ID=Rule4(IDList,self.probability)
                print("RULE 4")
            else:
                ID=0
        else:
            ID=calculateID(IDList,self.board[row][col].ID)
        return ID

    def setNeighbors(self,row,col,ID):
        for rule in self.neighborhood:
            nei_row = (row + rule[0])
            nei_col = (col + rule[1])

            if self.border is True:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                   continue
            else:
                if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                    nei_row = nei_row % self.dimX
                    nei_col = nei_col % self.dimY

            if(self.getCell(nei_row,nei_col).getID()==0):
                if(ID and ID!=1):
                    self.setCellNextState(nei_row,nei_col,ID)


    def evolveCell(self,row,col):
        ID=self.getNeighbors(row,col)
        self.setNeighbors(row,col,ID)

    def intBoardID(self):
        intBoard = array([[self.board[i][j].ID for j in range(0, self.dimY)] for i in range(0, self.dimX)])
        return intBoard

    def saveImage(self):
        img = Image.new('RGB', (self.dimX, self.dimX), "white")
        pixels = img.load()

        for i in range(0, self.dimX):
            for j in range(0, self.dimY):
                pixels[i, j] = colour_rule[self.board[i][j].getID()]
        img.save('CA_img.png')
        return img

    def writeToCSV(self):
        Tk().withdraw()
        name = asksaveasfilename(title='shot', defaultextension='.csv')
        with open(name, "w") as my_csv:
            my_csv.seek(0)
            csvWriter = writer(my_csv)
            arr=self.intBoardID()
            csvWriter.writerows(arr)

    def importFromCSV(self):
        Tk().withdraw()
        filename = askopenfilename()
        if(filename is ''):
            return

        with open(filename, mode='r') as csv_file:
            csv_reader = reader(csv_file, dialect=excel)
            result=[]
            for line in csv_reader:
                if len(line)>0:
                    result.append(line)
            print(result)
        self.dimX=len(result[0])
        self.dimY=len(result)

        for i in range(0, self.dimX):
            for j in range(0, self.dimY):
                ID=int(result[i][j])
                self.board[i][j]=Cell(i,j,ID,ID,colour_rule[ID])



