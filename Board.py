from Cell import *
import math
from csv import reader,writer,excel
from numpy import array, amax, unique
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from Curvature import *
from ast import literal_eval

MOORE_NEIGHBOURHOOD = [(-1,-1), (0,-1),  (+1,-1),
                       (-1,0),  (+1,0),
                       (-1,+1), (0,+1),  (+1,+1)]

VONNEUMANN_NEIGHBOURHOOD = [(0, -1),
                             (-1, 0), (+1, 0),
                             (0, +1)]
HEXAGONAL_LEFT = [(-1,-1), (-1,0), (0,-1), (0,1),(1,0),(1,1)]
HEXAGONAL_RIGHT = [(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0)]
PENTAGONAL_LEFT = [(-1,-1), (0,-1),
                       (-1,0),
                       (-1,+1), (0,+1)]
PENTAGONAL_RIGHT = [ (0,-1),  (+1,-1),
                      (+1,0),
                     (0,+1),  (+1,+1)]

RULE = [(-1,0),(0,+1),(+1,0)]
color_rule = {
    # Syntax is - cell value: (R, G, B)
    0: (255, 255, 255),
    1: (0,0,0),
    1000: (70, 70, 70)
    }

def generateColorRule(nrOfColours):
    for key in range(2,nrOfColours+2):
        color_rule[key]=(random.randrange(0,255,1,int),random.randrange(0,255,1,int),random.randrange(0,255,1,int))


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
        self.seeds=nrOfSeeds
        self.generate()
        # generateColorRule(nrOfSeeds)
        self.generateSeeds(nrOfSeeds)
        if(self.nrOfInclusions>0):
            if(radius[0]!=0 and radius[1]!=0):
                self.generateInclusions()


    def getCell(self,row,col):
        return self.board[row][col]

    def setCell(self,row,col,ID,nextID,color,phase):
        self.board[row][col]=Cell(row,col,ID,nextID,color,phase)

    def getMaxID(self):
        arr=array(self.intBoardID())
        return amax(arr)

    def setCurvature(self,curvature,probability):
        self.curvature=curvature
        self.probability=probability


    def setCellNextState(self,row,col,ID,color,phase):
        self.getCell(row,col).setNextID(ID)
        self.getCell(row,col).setColor(color)
        self.getCell(row,col).setPhase(phase)

    def generate(self):
        self.board=[[Cell(i,j,0,0,color_rule[0],0) for j in range(0,self.dimY)] for i in range(0,self.dimX)]

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
                        self.setCell(x,y,1,1,color_rule[1],0)


    def generateSeeds(self,nrOfSeeds):
        for s in range(2,nrOfSeeds+2):
            row=random.randrange(0,self.dimX,1,int)
            col=random.randrange(0,self.dimY,1,int)
            ID=s
            color=(random.randrange(0,255,1,int),random.randrange(0,255,1,int),random.randrange(0,255,1,int))
            if(self.getCell(row,col).ID==0):
                self.setCell(row,col,ID,ID,color,0)
        self.updateBoard()

    def addSeeds(self,nrOfSeeds,phase):
        startRange=self.getMaxID()+1
        print('Max ID: ',startRange)
        freeCells=[]
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                if(self.getCell(i,j).getID() == 0):
                    freeCells.append((i,j))
        print(freeCells)

        if(len(freeCells)<nrOfSeeds):
            nrOfSeeds=len(freeCells)-10

        for seed in range(startRange,nrOfSeeds+startRange):
            coord=random.choice(freeCells)
            print('Coords: ', coord)
            color=(random.randrange(0,255,1,int),random.randrange(0,255,1,int),random.randrange(0,255,1,int))
            self.setCell(coord[0], coord[1], seed, seed, color,phase)

        print('After seeding')
        self.updateBoard()

    def markBoundries(self):
        boundrylength=0
        neighbors=[]
        colors=[]
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                for rule in RULE:
                    nei_row = (i + rule[0])
                    nei_col = (j + rule[1])

                    if nei_row < 0 or nei_row >= self.dimX or nei_col < 0 or nei_col >= self.dimY:
                            nei_row = nei_row % self.dimX
                            nei_col = nei_col % self.dimY

                    neighbors.append(self.getCell(nei_row,nei_col).getID())
                    colors.append(self.getCell(nei_row,nei_col).getColor())
                print(neighbors)
                ID=self.getCell(i,j).getID()
                if neighbors.count(self.getCell(i,j).getID())<3:
                    if (neighbors[0]!= ID) and (neighbors[1] == ID) and (neighbors[2]==ID):
                        print('pionowo')
                    # elif(neighbors[0]== ID) and (neighbors[1] == ID) and (neighbors[2]!=ID):
                    #     print('pionowo')
                    elif(neighbors[0]!= ID) and (neighbors[1] == ID) and (neighbors[2]!=ID):
                        print('pionowo')
                    else:
                        self.getCell(i, j).setColor(color_rule[1000])
                        boundrylength += 1

                neighbors.clear()
                colors.clear()

        self.updateBoard()
        return boundrylength

    def removeSeed(self, color):
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                if(self.getCell(i,j).getColor() == color):
                    self.board[i][j]=Cell(i,j,0,0,color_rule[0],0)
        self.updateBoard()


    def iteration(self):
        empty_cell=0
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                if(self.getCell(i,j).getID() == 0):
                    # print("before evolve cell")
                    empty_cell=empty_cell+self.evolveCell(i,j)
        self.updateBoard()
        return empty_cell

    def updateBoard(self):
        for i in range(0,self.dimX):
            for j in range(0,self.dimY):
                self.board[i][j].update()
        self.saveImage()


    def getNeighbors(self,row,col):
        IDList = []
        colors={}
        phases={}
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
            colors[self.getCell(nei_row,nei_col).getID()]=self.getCell(nei_row,nei_col).getColor()
            phases[self.getCell(nei_row,nei_col).getID()]=self.getCell(nei_row,nei_col).getPhase()

        if(self.curvature==True):
            # print("Doing curvature")
            if(Rule1(IDList)):
                ID=Rule1(IDList)
                # print("RULE 1")
            elif(Rule2(IDList)):
                ID=Rule2(IDList)
                # print("RULE 2")
            elif(Rule3(IDList)):
                ID=Rule3(IDList)
                # print("RULE 3")
            elif(Rule4(IDList,self.probability)):
                ID=Rule4(IDList,self.probability)
                if(ID==0):
                    colors[ID] = (255, 255, 255)
                    phases[ID] = 0
                    # print("RULE 4")
            else:
                # print("Not ID choosed")
                ID=0
                colors[ID]=(255,255,255)
                phases[ID]=0
        else:
            ID=calculateID(IDList)
        # print(f'{ID} {colors} {phases}')
        return ID,colors[ID],phases[ID]

    def setNeighbors(self,row,col,ID,color,phase):
        if(ID and ID!=1):
            # print('Nei color, ID: ',color, ID)
            self.setCellNextState(row,col,ID,color,phase)

    def evolveCell(self,row,col):
        ID,color,phase=self.getNeighbors(row,col)
        self.setNeighbors(row,col,ID,color,phase)
        if(ID>0):
            return 1
        else:
            return 0

    def intBoardID(self):
        intBoard = array([[self.board[i][j].ID for j in range(0, self.dimY)] for i in range(0, self.dimX)])
        return intBoard

    def boardCellsStatus(self):
        Board = array([[self.board[i][j] for j in range(0, self.dimY)] for i in range(0, self.dimX)])
        return Board

    def saveImage(self):
        img = Image.new('RGB', (self.dimX, self.dimX), "white")
        pixels = img.load()

        for i in range(0, self.dimX):
            for j in range(0, self.dimY):
                pixels[i, j] = self.getCell(i,j).getColor()
        img.save('CA_img.png')
        return img

    def writeToCSV(self):
        Tk().withdraw()
        name = asksaveasfilename(title='shot', defaultextension='.csv')
        with open(name, "w") as my_csv:
            my_csv.seek(0)
            csvWriter = writer(my_csv)
            arr=self.boardCellsStatus()
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
                cell=result[i][j].split(';')
                ID=int(cell[2])
                color=literal_eval(cell[3])
                phase=int(cell[4])
                print(f'cell: id-{ID}, colour-{color}, phase-{phase}')
                self.setCell(i,j,ID,ID,color,phase)
                self.board[i][j].setPhase(phase)



