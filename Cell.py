

class Cell:
    def __init__(self,row,col,ID,nextID,color,phase):
        self.row=row
        self.col=col
        self.ID=ID
        self.nextID=nextID
        self.color=color
        self.phase=phase

    def __repr__(self):
        return f'{self.row};{self.col};{self.ID};{self.color};{self.phase}'

    def setID(self,ID):
        self.ID=ID

    def setNextID(self,nextID):
        self.nextID=nextID

    def getID(self):
        return self.ID

    def setColor(self,color):
        self.color=color

    def getColor(self):
        return self.color

    def setPhase(self, phase):
        self.phase=phase

    def getPhase(self):
        return self.phase

    def update(self):
        self.ID=self.nextID