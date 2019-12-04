

class Cell:
    def __init__(self,row,col,ID,nextID,colour):
        self.row=row
        self.col=col
        self.ID=ID
        self.nextID=nextID
        self.colour=colour

    def __repr__(self):
        return f'{self.ID}'

    def setID(self,ID):
        self.ID=ID

    def setNextID(self,nextID):
        self.nextID=nextID

    def getID(self):
        return self.ID

    def setColour(self,colour):
        self.colour=colour

    def update(self):
        self.ID=self.nextID