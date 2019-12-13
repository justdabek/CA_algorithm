import random

def Rule1(IDList):
    mainCellID=IDList[4]

    if(IDList.count(mainCellID)>=5):
        return True
    else:
        return False

def Rule2(IDList):
    mainCellID=IDList[4]

    NearestNeighborsList=[IDList[1],IDList[3],IDList[5],IDList[7]]

    if(NearestNeighborsList.count(mainCellID)>=3):
        return True
    else:
        return False

def Rule3(IDList):
    mainCellID=IDList[4]

    FurtherNeighborsList=[IDList[0],IDList[2],IDList[6],IDList[8]]

    if(FurtherNeighborsList.count(mainCellID)>=3):
        return True
    else:
        return False

def Rule4(IDList,probability):
    mainCellID=IDList[4]
    n=random.randrange(0, 100, 1, int)

    if(n<=probability):
        return calculateID(IDList,mainCellID)
    else:
        return False

def calculateID(IDList,cellID):
    NO_CELL = 0
    set_id = 0
    most_frequent = 0
    unique_vals = set(IDList)
    if len(IDList) > 0:
        for val in unique_vals:
            if val != NO_CELL and val!=1:
                frequence = IDList.count(val)
                if frequence == most_frequent:
                    set_id = cellID
                elif frequence > most_frequent:
                    most_frequent = frequence
                    set_id = val
    return set_id